import time
import json
import unittest

from google.protobuf import json_format
from fds.protobuf.stach.Package_pb2 import Package
from urllib3.response import HTTPResponse

from fds.analyticsapi.engines.api.calculations_api import CalculationsApi
from fds.analyticsapi.engines.api.optimizations_api import OptimizationsApi
from fds.analyticsapi.engines.models.axioma_equity_optimization_parameters import AxiomaEquityOptimizationParameters
from fds.analyticsapi.engines.models.strategy import Strategy
from fds.analyticsapi.engines.models.account import Account
from fds.analyticsapi.engines.models.optimization import Optimization
from fds.analyticsapi.engines.models.output_types import OutputTypes
from fds.analyticsapi.engines.models.trades_list import TradesList
from fds.analyticsapi.engines.models.calculation_status import CalculationStatus

import common_parameters
from common_functions import CommonFunctions

class TestOptimizerApi(unittest.TestCase):

    def setUp(self):
        self.api_client = CommonFunctions.build_api_client()
        self.calculations_api = CalculationsApi(self.api_client)
        self.create_response = self.run_calculation()
        self.status_response = None

    def run_calculation(self):
        optimizer_api = OptimizationsApi(self.api_client)
        strategy = Strategy(id="Client:test")
        account = Account(id="Client:/analytics/nyim/TEST.ACCT")
        optimization = Optimization(riskmodeldate="0M", backtestdate="0M")
        trade_list = TradesList(identifiertype="Asset", includecash=False)
        output_types = OutputTypes(trades=trade_list)
        parameters = AxiomaEquityOptimizationParameters(strategy=strategy, account=account, optimization=optimization, outputtypes=output_types)
        response = optimizer_api.run_axioma_optimization_with_http_info(axioma_equity_optimization_parameters=parameters)
        return response

    def test_create_calculation(self):
        self.assertEqual(self.create_response[1], 202, "Response should be 202 - Accepted")
        self.assertEqual(self.create_response[0], None, "Response data should be null.")

    def test_get_calculation_status(self):
        calculation_id = self.create_response[2].get("location").split("/")[-1]
        self.status_response = self.calculations_api.get_calculation_status_by_id_with_http_info(calculation_id)
        self.assertEqual(self.status_response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(self.status_response[0]), CalculationStatus, "Response should be of CalculationStatus type")
        self.assertEqual(type(self.status_response[0].pa), dict, "Response should be of dictionary type")

if __name__ == '__main__':
    unittest.main()
