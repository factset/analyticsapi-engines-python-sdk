import time
import os
import uuid
import pandas as pd

from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api.axp_optimizer_api import AXPOptimizerApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.axioma_equity_optimization_parameters_root import AxiomaEquityOptimizationParametersRoot
from fds.analyticsapi.engines.model.axioma_equity_optimizer_strategy import AxiomaEquityOptimizerStrategy
from fds.analyticsapi.engines.model.optimizer_account import OptimizerAccount
from fds.analyticsapi.engines.model.axioma_equity_optimization_parameters import AxiomaEquityOptimizationParameters
from fds.analyticsapi.engines.model.optimizer_output_types import OptimizerOutputTypes
from fds.analyticsapi.engines.model.optimizer_trades_list import OptimizerTradesList
from fds.analyticsapi.engines.model.optimization import Optimization
from fds.protobuf.stach.extensions.StachExtensionFactory import StachExtensionFactory
from fds.protobuf.stach.extensions.StachVersion import StachVersion

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
        #     "data": {
        #         "strategy": {
        #             "id": "Client:/Optimizer/CN_TEST"
        #         },
        #         "account": {
        #             "id": "CLIENT:/OPTIMIZER/IBM.ACCT"
        #         },
        #         "optimization": {
        #             "riskmodeldate": "09/01/2020",
        #             "backtestdate": "09/01/2020",
        #             "cashflow": "0"
        #         },
        #         "outputtypes": {
        #             "trades": {
        #                 "identifiertype": "SedolChk",
        #                 "includecash": false
        #             }
        #         }
        #     }
        # }
        axp_optimizer_strategy = AxiomaEquityOptimizerStrategy(
            id="Client:/Optimizer/CN_TEST")
        axp_optimizer_account = OptimizerAccount(
            id="CLIENT:/OPTIMIZER/IBM.ACCT")
        axp_optimizer_optimization = Optimization(
            risk_model_date="09/01/2020",
            backtest_date="09/01/2020",
            cashflow="0"
        )
        axp_optimizer_trades_list = OptimizerTradesList(
            identifier_type="SedolChk", include_cash=False)
        axp_optimizer_output_types = OptimizerOutputTypes(
            trades=axp_optimizer_trades_list)
        axp_optimizer_parameters = AxiomaEquityOptimizationParameters(
            strategy=axp_optimizer_strategy,
            output_types=axp_optimizer_output_types,
            account=axp_optimizer_account,
            optimization=axp_optimizer_optimization
        )
        axp_optimization_parameters_root = AxiomaEquityOptimizationParametersRoot(
            data=axp_optimizer_parameters)

        axp_optimizations_api = AXPOptimizerApi(api_client)

        post_and_optimize_response = axp_optimizations_api.post_and_optimize(
            axioma_equity_optimization_parameters_root=axp_optimization_parameters_root
        )

        if post_and_optimize_response[1] == 201:
            output_optimization_result(post_and_optimize_response[0]['data'])
        else:
            optimization_id = post_and_optimize_response[2]["X-Factset-Api-Calculation-Id"]
            print("Calculation Id: " + optimization_id)

            status_response = axp_optimizations_api.get_optimization_status_by_id(id=optimization_id)

            while status_response[1] == 202:
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = axp_optimizations_api.get_optimization_status_by_id(optimization_id)

            if status_response[1] == 201:
                print("Optimization Id: " + optimization_id + " Succeeded!!!")
                result_response = axp_optimizations_api.get_optimization_result(id=optimization_id)
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
    stachBuilder = StachExtensionFactory.get_row_organized_builder(
        StachVersion.V2)
    stachExtension = stachBuilder.add_table("tradesTable", result['trades']).build()
    # stachExtension = stachBuilder.add_table("optimalsTable", result['trades']).build()
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
