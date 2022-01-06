import time
import os
import uuid
import pandas as pd

from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api.afi_optimizer_api import AFIOptimizerApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.afi_optimizer_strategy import AFIOptimizerStrategy
from fds.analyticsapi.engines.model.afi_optimization_parameters import AFIOptimizationParameters
from fds.analyticsapi.engines.model.afi_optimization_parameters_root import AFIOptimizationParametersRoot
from fds.analyticsapi.engines.model.optimizer_output_types import OptimizerOutputTypes
from fds.analyticsapi.engines.model.optimizer_trades_list import OptimizerTradesList
from fds.protobuf.stach.extensions.StachExtensionFactory import StachExtensionFactory
from fds.protobuf.stach.extensions.StachVersion import StachVersion

from urllib3 import Retry

host = os.environ['FACTSET_HOST']
fds_username = os.environ['FACTSET_USERNAME']
fds_api_key = os.environ['FACTSET_API_KEY']


def main():
    config = Configuration()
    config.host = host
    config.username = fds_username
    config.password = fds_api_key
    config.discard_unknown_keys = True
    # add proxy and/or disable ssl verification according to your development environment
    # config.proxy = "<proxyUrl>"
    config.verify_ssl = False

    # Setting configuration to retry api calls on http status codes of 429 and 503.
    config.retries = Retry(total=3, status=3, status_forcelist=frozenset([429, 503]), backoff_factor=2,
                           raise_on_status=False)

    api_client = ApiClient(config)

    try:
        # {
        # 	"data": {
        #         "strategy": {
        #             "id": "CLIENT:/Analytics_api/AFIAPISIMPLE"
        #         },
        #         "outputTypes": {
        #             "trades": {
        #                 "identifierType": "Asset",
        #                 "includeCash": false
        #             }
        #         }
        #     }
        # }
        afi_optimizer_strategy = AFIOptimizerStrategy(
            id="CLIENT:/Analytics_api/AFIAPISIMPLE")
        afi_optimizer_trades_list = OptimizerTradesList(
            identifier_type="Asset", include_cash=False)
        afi_optimizer_output_types = OptimizerOutputTypes(
            trades=afi_optimizer_trades_list)
        afi_optimization_parameters = AFIOptimizationParameters(
            afi_optimizer_strategy, afi_optimizer_output_types)
        afi_optimization_parameters_root = AFIOptimizationParametersRoot(
            data=afi_optimization_parameters)
        # uncomment the below code line to setup cache control; max-stale=0 will be a fresh adhoc run and the max-stale value is in seconds.
        # Results are by default cached for 12 hours; Setting max-stale=300 will fetch a cached result which is 5 minutes older.
        # cache_control = "max-stale=0"
        afi_optimizations_api = AFIOptimizerApi(api_client)
        
        post_and_optimize_response = afi_optimizations_api.post_and_optimize(
            afi_optimization_parameters_root=afi_optimization_parameters_root)
        # comment the above line and uncomment the below line to run the request with the cache_control header defined earlier
        # post_and_optimize_response = afi_optimizations_api.post_and_optimize(
            # afi_optimization_parameters_root=afi_optimization_parameters_root, cache_control=cache_control)
        if post_and_optimize_response[1] == 201:
            output_optimization_result(post_and_optimize_response[0]['data'])
        else:
            optimization_id = post_and_optimize_response[2]["X-Factset-Api-Calculation-Id"]
            print("Calculation Id: " + optimization_id)

            status_response = afi_optimizations_api.get_optimization_status_by_id(id=optimization_id)

            while status_response[1] == 202:
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = afi_optimizations_api.get_optimization_status_by_id(optimization_id)

            if status_response[1] == 201:
                print("Optimization Id: " + optimization_id + " Succeeded!!!")
                result_response = afi_optimizations_api.get_optimization_result(id=optimization_id)
                output_optimization_result(result_response[0]['data'])
            else:
                print("Optimization Id:" + optimization_id + " Failed!!!")
                print("Error message : " + status_response[0].errors)

    except ApiException as e:
        print("Api exception Encountered")
        print(e)
        exit()


def output_optimization_result(result):
    print("Optimization Result")
    stachBuilder = StachExtensionFactory.get_row_organized_builder(
        StachVersion.V2)
    stachExtension = stachBuilder.add_table("tradesTable", result['trades']).build()
    # stachExtension = stachBuilder.add_table("optimalsTable", result['optimal']).build()
    dataFramesList = stachExtension.convert_to_dataframe()
    print(dataFramesList)


def generate_excel(data_frames_list):
    for dataFrame in data_frames_list:
        writer = pd.ExcelWriter(  # pylint: disable=abstract-class-instantiated
            str(uuid.uuid1()) + ".xlsx")
        dataFrame.to_excel(excel_writer=writer)
        writer.save()
        writer.close()


if __name__ == '__main__':
    main()
