import time

from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.models.axioma_equity_optimization_parameters import AxiomaEquityOptimizationParameters
from fds.analyticsapi.engines.api.optimizations_api import OptimizationsApi
from fds.analyticsapi.engines.models.strategy import Strategy
from fds.analyticsapi.engines.models.strategy_overrides import StrategyOverrides
from fds.analyticsapi.engines.models.account import Account
from fds.analyticsapi.engines.models.account_overrides import AccountOverrides
from fds.analyticsapi.engines.models.optimization import Optimization
from fds.analyticsapi.engines.models.optimal_holdings import OptimalHoldings
from fds.analyticsapi.engines.models.output_types import OutputTypes
from fds.analyticsapi.engines.models.trades_list import TradesList

from google.protobuf.json_format import MessageToJson

from urllib3 import Retry

host = "https://api.factset.com"
user_serial = "<username-serial>"
password = "<apiKey>"

# Enter the name of the AXP2 document/strategy (required) to optimize
strategy_id = "Client:test"

# Enter an account (optional) to override the portfolio, benchmark, risk model, currency, and calendar
# settings defined in the universe section of the document/strategy
account_id = "Client:/analytics/nyim/TEST.ACCT"

# Optionally override what's defined in the document/strategy and account (optional) by specifying in-line the
# portfolio, benchmark, and/or risk model
portfolio_override = ""
benchmark_override = ""
risk_model_id_override = ""
account_overrides = AccountOverrides(portfolio=portfolio_override, benchmark=benchmark_override, riskmodelid=risk_model_id_override)

# Optionally override the risk model date, back test date, and cash flow
optimization_risk_model_date = "0M"
optimization_back_test_date = "0M"
cash_flow = ""

# Optionally override what Objectives, Tax, and/or Transaction Cost setting to make active or,
# which Constraint(s) to enable or disable.  For a complete description of strategy override usage,
# please see https://developer.factset.com/api-catalog/axioma-equity-api
strategy_overrides = StrategyOverrides()

# Specify what and how output (required) from optimization should be returned.  For a full list of available
# output types, please see https://developer.factset.com/api-catalog/axioma-equity-api
trade_list_identifier_type = "Asset"
trade_list_include_cash = False
trade_list = TradesList(identifiertype=trade_list_identifier_type, includecash=trade_list_include_cash)
optimal_holdings = OptimalHoldings(identifiertype="Ticker", includecash=False, excludezero=True)


def main():
    config = Configuration()
    config.host = host
    config.username = user_serial
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
        strategy = Strategy(id=strategy_id, overrides=strategy_overrides)
        account = Account(id=account_id, overrides=account_overrides)
        optimization = Optimization(riskmodeldate=optimization_risk_model_date, backtestdate=optimization_back_test_date, cashflow=cash_flow)
        output_types = OutputTypes(trades=trade_list, optimal=OptimalHoldings)
        parameters = AxiomaEquityOptimizationParameters(strategy=strategy, account=account, optimization=optimization, outputtypes=output_types)
        run_calculation_response = optimizer_api.run_axioma_optimization_with_http_info(axioma_equity_optimization_parameters=parameters)

        if (run_calculation_response[1] == 201):
            print("Optimization report succeeded!")
            print(MessageToJson(run_calculation_response[0]))  # To print the response as a JSON
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
                print(MessageToJson(run_calculation_response[0]))  # To print the response as a JSON
            else:
                print("Optimization report failed")

    except ApiException as e:
        print("Api exception Encountered")
        print(e)
        exit()


if __name__ == '__main__':
    main()
