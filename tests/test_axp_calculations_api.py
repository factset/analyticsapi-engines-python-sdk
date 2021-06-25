import unittest
import time

from fds.analyticsapi.engines.api.axp_optimizer_api import AXPOptimizerApi
from fds.analyticsapi.engines.model.axioma_equity_optimization_parameters import AxiomaEquityOptimizationParameters
from fds.analyticsapi.engines.model.axioma_equity_optimization_parameters_root import AxiomaEquityOptimizationParametersRoot
from fds.analyticsapi.engines.model.axioma_equity_optimizer_strategy import AxiomaEquityOptimizerStrategy
from fds.analyticsapi.engines.model.axioma_equity_optimizer_strategy_overrides import AxiomaEquityOptimizerStrategyOverrides
from fds.analyticsapi.engines.model.optimizer_account import OptimizerAccount
from fds.analyticsapi.engines.model.optimization import Optimization
from fds.analyticsapi.engines.model.optimizer_trades_list import OptimizerTradesList
from fds.analyticsapi.engines.model.optimizer_output_types import OptimizerOutputTypes


from common_functions import CommonFunctions
from api_workflow import run_api_workflow_with_assertions


class TestAxpOptimizationsApi(unittest.TestCase):
    def setUp(self):
        api_client = CommonFunctions.build_api_client()
        self.axp_optimizer_api = AXPOptimizerApi(api_client)

    def test_single_unit_scenario(self):
        create_step_name = "create_calculation"
        read_status_step_name = "read_status"
        read_result_step_name = "read_result"

        def create_calculation(test_context):
            print("Creating single unit calculation")
            axp_strategy = AxiomaEquityOptimizerStrategy(id="Client:/Optimizer/TAXTEST")
            axp_account = OptimizerAccount(id="BENCH:SP50")
            optimization = Optimization(risk_model_date="09/01/2020",backtest_date="09/01/2020")
            trades_list = OptimizerTradesList(identifier_type="SedolChk", include_cash=False)
            output_types = OptimizerOutputTypes(trades=trades_list)

            axp_calculation_parameters = AxiomaEquityOptimizationParameters(strategy=axp_strategy, account=axp_account,
                optimization=optimization, output_types=output_types)

            axp_calculation_parameter_root = AxiomaEquityOptimizationParametersRoot(
                data=axp_calculation_parameters)

            post_and_calculate_response = self.axp_optimizer_api.post_and_optimize(
                axioma_equity_optimization_parameters_root=axp_calculation_parameter_root
            )

            self.assertTrue(post_and_calculate_response[1] == 201 or post_and_calculate_response[1] == 202,
                            "Response for create_calculation should have been 201 or 202")

            if post_and_calculate_response[1] == 201:
                return {
                    "continue_workflow": False,
                    "next_request": None,
                    "test_context": None
                }
            elif post_and_calculate_response[1] == 202:
                test_context["calculation_id"] = post_and_calculate_response[2]["X-Factset-Api-Calculation-Id"]
                return {
                    "continue_workflow": True,
                    "next_request": read_status_step_name,
                    "test_context": test_context
                }

        def read_calculation_status(test_context):
            print("Reading single unit calculation status")
            calculation_id = test_context["calculation_id"]
            print("Calculation Id: " + calculation_id)

            status_response = self.axp_optimizer_api.get_optimization_status_by_id(id=calculation_id)

            self.assertTrue(status_response[1] == 202 or status_response[1] == 201)

            while status_response[1] == 202:
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = self.axp_optimizer_api.get_optimization_status_by_id(id=calculation_id)

            return {
                "continue_workflow": True,
                "next_request": read_result_step_name,
                "test_context": test_context
            }

        def read_calculation_result(test_context):
            calculation_id = test_context["calculation_id"]
            result_response = self.axp_optimizer_api.get_optimization_result(id=calculation_id)
            self.assertEqual(result_response[1], 200, "Get calculation result should have succeeded")

        workflow_specification = {
            create_step_name: create_calculation,
            read_status_step_name: read_calculation_status,
            read_result_step_name: read_calculation_result
        }
        starting_request = workflow_specification['create_calculation']
        starting_test_context = {}
        run_api_workflow_with_assertions(
            workflow_specification, starting_request, starting_test_context)


if __name__ == '__main__':
    unittest.main(failfast=True)
