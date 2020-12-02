import time
import unittest

from fds.analyticsapi.engines.api.optimizations_api import OptimizationsApi
from fds.analyticsapi.engines.models.axioma_equity_optimization_parameters import AxiomaEquityOptimizationParameters
from fds.analyticsapi.engines.models.strategy import Strategy
from fds.analyticsapi.engines.models.account import Account
from fds.analyticsapi.engines.models.optimization import Optimization
from fds.analyticsapi.engines.models.output_types import OutputTypes
from fds.analyticsapi.engines.models.trades_list import TradesList

import common_parameters
from common_functions import CommonFunctions


class TestOptimizerApi(unittest.TestCase):

    def setUp(self):
        self.api_client = CommonFunctions.build_api_client()

    def test_normal_workflow(self):
        optimizer_api = OptimizationsApi(self.api_client)
        strategy = Strategy(id="Client:test")
        account = Account(id="Client:/analytics/nyim/TEST.ACCT")
        optimization = Optimization(riskmodeldate="0M", backtestdate="0M")
        trade_list = TradesList(identifiertype="Asset", includecash=False)
        output_types = OutputTypes(trades=trade_list)
        parameters = AxiomaEquityOptimizationParameters(strategy=strategy, account=account, optimization=optimization, outputtypes=output_types)
        response = optimizer_api.run_axioma_optimization_with_http_info(axioma_equity_optimization_parameters=parameters)

        if (response[1] == 201):
            self.assertEqual(response[2].get("content-type"), "application/json")
        elif (response[1] == 202):
            optimization_id = response[2].get("location").split("/")[-1]
            while (response[1] == 202):
                age_value = response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                    time.sleep(int(max_age))
                else:
                    time.sleep(5)
                response = optimizer_api.get_axioma_optimization_by_id_with_http_info(optimization_id)

            self.assertEqual(response[2].get("content-type"), "application/json")
        else:
            assert False, "Optimizer workflow did not succeed"

if __name__ == '__main__':
    unittest.main()
