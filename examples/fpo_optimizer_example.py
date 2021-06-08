import time
import pandas as pd
import os
import uuid

from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api.fpo_optimizer_api import FPOOptimizerApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.fpo_optimization_parameters_root import FPOOptimizationParametersRoot
from fds.analyticsapi.engines.model.optimizer_strategy import OptimizerStrategy
from fds.analyticsapi.engines.model.pa_doc import PaDoc
from fds.analyticsapi.engines.model.fpo_account import FPOAccount
from fds.analyticsapi.engines.model.fpo_optimization_parameters import FPOOptimizationParameters
from fds.analyticsapi.engines.model.optimizer_output_types import OptimizerOutputTypes
from fds.analyticsapi.engines.model.optimizer_trades_list import OptimizerTradesList
from fds.analyticsapi.engines.model.optimization import Optimization

from urllib3 import Retry

host = "https://api.factset.com"
username = os.environ["ANALYTICS_API_USERNAME_SERIAL"]
password = os.environ["ANALYTICS_API_PASSWORD"]


def main():
    config = Configuration()
    config.host = host
    config.username = username
    config.password = password
    # add proxy and/or disable ssl verification according to your development environment
    # config.proxy = "<proxyUrl>"
    config.verify_ssl = False

    # Setting configuration to retry api calls on http status codes of 429 and 503.
    config.retries = Retry(total=3, status=3, status_forcelist=frozenset([429, 503]), backoff_factor=2,
                           raise_on_status=False)

    api_client = ApiClient(config)

    try:
        # {
        #     "strategy": {
        #         "id": "Client:/analytics_api/dbui_simple_strategy"
        #     },
        #     "account": {
        #         "id": "CLIENT:/FPO/1K_MAC_AMZN_AAPL.ACCT",
        #         "padocument": {
        #             "id": "CLIENT:/FPO/FPO_MASTER"
        #         }
        #     },
        #     "optimization": {
        #         "riskmodeldate": "0M",
        #         "backtestdate": "0M"
        #     },
        #     "outputtypes": {
        #         "trades": {
        #             "identifiertype": "Asset",
        #             "includecash": false
        #         }
        #     }
        # }
        fpo_optimizer_strategy = OptimizerStrategy(id="Client:/analytics_api/dbui_simple_strategy")
        fpo_pa_doc = PaDoc("CLIENT:/FPO/FPO_MASTER")
        fpo_optimizer_account = FPOAccount(fpo_pa_doc, id="CLIENT:/FPO/1K_MAC_AMZN_AAPL.ACCT")
        fpo_optimizer_optimization = Optimization(
            risk_model_date="0M",
            backtest_date="0M",
        )
        fpo_optimizer_trades_list = OptimizerTradesList(identifier_type="Asset", include_cash=False)
        fpo_optimizer_output_types = OptimizerOutputTypes(trades=fpo_optimizer_trades_list)
        fpo_optimizer_parameters = FPOOptimizationParameters(
            fpo_optimizer_strategy,
            fpo_optimizer_output_types,
            account=fpo_optimizer_account,
            optimization=fpo_optimizer_optimization
        )
        fpo_optimization_parameters_root = FPOOptimizationParametersRoot(data=fpo_optimizer_parameters)

        fpo_optimizations_api = FPOOptimizerApi(api_client)

        post_and_optimize_response = fpo_optimizations_api.post_and_optimize(
            fpo_optimization_parameters_root=fpo_optimization_parameters_root,
            _return_http_data_only=False
        )

        if post_and_optimize_response[1] == 201:
            output_optimization_result(post_and_optimize_response[0]['data'])
        else:
            optimization_id = post_and_optimize_response[0].data.id
            print("Calculation Id: " + optimization_id)

            status_response = fpo_optimizations_api.get_optimization_status_by_id(id=optimization_id,
                                                                                  _return_http_data_only=False)

            while status_response[1] == 202:
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = fpo_optimizations_api.get_optimization_status_by_id(optimization_id,
                                                                                      _return_http_data_only=False)

            if status_response[1] == 201:
                print("Optimization Id: " + optimization_id + " Succeeded!!!")
                result_response = fpo_optimizations_api.get_optimization_result(id=optimization_id,
                                                                                _return_http_data_only=False)
                output_optimization_result(result_response[0]['data'])
            else:
                print("Optimization Id:" + optimization_id + " Failed!!!")
                print("Error message : " + status_response[0].error)

    except ApiException as e:
        print("Api exception Encountered")
        print(e)
        exit()


def output_optimization_result(result):
    print("Optimization Result")
    print(result)


def generate_excel(data_frames_list):
    for dataFrame in data_frames_list:
        writer = pd.ExcelWriter(str(uuid.uuid1()) + ".xlsx") # pylint: disable=abstract-class-instantiated
        dataFrame.to_excel(excel_writer=writer)
        writer.save()
        writer.close()


if __name__ == '__main__':
    main()
