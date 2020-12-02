import time

from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.models.axioma_equity_optimization_parameters import AxiomaEquityOptimizationParameters
from fds.analyticsapi.engines.api.optimizations_api import OptimizationsApi
from fds.analyticsapi.engines.models.strategy import Strategy
from fds.analyticsapi.engines.models.account import Account
from fds.analyticsapi.engines.models.optimization import Optimization
from fds.analyticsapi.engines.models.output_types import OutputTypes
from fds.analyticsapi.engines.models.trades_list import TradesList

from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import MessageToDict

from urllib3 import Retry

host = "https://api.factset.com"
username = "<username-serial>"
password = "<apiKey>"

strategy_id = "Client:test"
account_id = "Client:/analytics/nyim/TEST.ACCT"
optimization_risk_model_date = "0M"
optimization_back_test_date = "0M"
trade_list_identifier_type = "Asset"
trade_list_include_cash = False


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
        optimizer_api = OptimizationsApi(api_client)
        strategy = Strategy(id=strategy_id)
        account = Account(id=account_id)
        optimization = Optimization(riskmodeldate=optimization_risk_model_date, backtestdate=optimization_back_test_date)
        trade_list = TradesList(identifiertype=trade_list_identifier_type, includecash=trade_list_include_cash)
        output_types = OutputTypes(trades=trade_list)
        parameters = AxiomaEquityOptimizationParameters(strategy=strategy, account=account, optimization=optimization, outputtypes=output_types)
        run_calculation_response = optimizer_api.run_axioma_optimization_with_http_info(axioma_equity_optimization_parameters=parameters)

        if (run_calculation_response[1] == 201):
            print("Optimization report succeeded!")
            print(MessageToJson(run_calculation_response[0])) # To print the response as a JSON
            # print(MessageToDict(run_calculation_response[0])) # To print the response as a Dictionary
        elif (run_calculation_response[1] == 202):
            optimization_id = run_calculation_response[2].get("location").split("/")[-1]
            print("Optimization Id: " + optimization_id)
            status_response = optimizer_api.get_axioma_optimization_by_id_with_http_info(optimization_id)

            while status_response[1] == 202:
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = optimizer_api.get_axioma_optimization_by_id_with_http_info(optimization_id)

            if (status_response[1] == 200):
                print("Optimization report succeeded!")
                print(MessageToJson(run_calculation_response[0])) # To print the response as a JSON
                # print(MessageToDict(run_calculation_response[0])) # To print the response as a Dictionary
            else:
                print("Optimization report failed")

    except ApiException as e:
        print("Api exception Encountered")
        print(e)
        exit()


if __name__ == '__main__':
    main()
