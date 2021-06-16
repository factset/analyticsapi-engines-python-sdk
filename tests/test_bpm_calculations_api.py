import unittest
import time

from fds.analyticsapi.engines.api.bpm_optimizer_api import BPMOptimizerApi
from fds.analyticsapi.engines.model.bpm_optimization_parameters import BPMOptimizationParameters
from fds.analyticsapi.engines.model.bpm_optimization_parameters_root import BPMOptimizationParametersRoot
from fds.analyticsapi.engines.model.bpm_optimizer_strategy import BPMOptimizerStrategy
from fds.analyticsapi.engines.model.bpm_optimizer_strategy_overrides import BPMOptimizerStrategyOverrides
from fds.analyticsapi.engines.model.optimizer_account import OptimizerAccount
from fds.analyticsapi.engines.model.bpm_optimization import BPMOptimization
from fds.analyticsapi.engines.model.optimizer_trades_list import OptimizerTradesList
from fds.analyticsapi.engines.model.optimizer_output_types import OptimizerOutputTypes


from common_functions import CommonFunctions
from api_workflow import run_api_workflow_with_assertions


class TestBpmOptimizationsApi(unittest.TestCase):
    def setUp(self):
        api_client = CommonFunctions.build_api_client()
        self.bpm_optimizer_api = BPMOptimizerApi(api_client)

    def test_single_unit_scenario(self):
        create_step_name = "create_calculation"
        read_status_step_name = "read_status"
        read_result_step_name = "read_result"

        def create_calculation(test_context):
            print("Creating single unit calculation")
            bpm_strategy = BPMOptimizerStrategy(id="CLIENT:/Aapi/Optimizers/BPMAPISIMPLE")
            bpm_account = OptimizerAccount(id="BENCH:SP50")
            optimization = BPMOptimization(risk_model_date="09/01/2008",backtest_date="09/01/2008")
            trades_list = OptimizerTradesList(identifier_type="Asset", include_cash=False)
            output_types = OptimizerOutputTypes(trades=trades_list)

            bpm_calculation_parameters = BPMOptimizationParameters(strategy=bpm_strategy, account=bpm_account,
                optimization=optimization, output_types=output_types)

            bpm_calculation_parameter_root = BPMOptimizationParametersRoot(
                data=bpm_calculation_parameters)

            post_and_calculate_response = self.bpm_optimizer_api.post_and_optimize(
                bpm_optimization_parameters_root=bpm_calculation_parameter_root, _return_http_data_only=False)

            self.assertTrue(post_and_calculate_response[1] == 201 or post_and_calculate_response[1] == 202,
                            "Response for create_calculation should have been 201 or 202")

            if post_and_calculate_response[1] == 201:
                return {
                    "continue_workflow": False,
                    "next_request": None,
                    "test_context": None
                }
            elif post_and_calculate_response[1] == 202:
                test_context["calculation_id"] = post_and_calculate_response[0].data.id
                return {
                    "continue_workflow": True,
                    "next_request": read_status_step_name,
                    "test_context": test_context
                }

        def read_calculation_status(test_context):
            print("Reading single unit calculation status")
            calculation_id = test_context["calculation_id"]
            print("Calculation Id: " + calculation_id)

            status_response = self.bpm_optimizer_api.get_optimization_status_by_id(id=calculation_id,
                                                                                    _return_http_data_only=False)

            self.assertTrue(status_response[1] == 202 or status_response[1] == 201)

            while status_response[1] == 202:
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = self.bpm_optimizer_api.get_optimization_status_by_id(id=calculation_id,
                                                                                        _return_http_data_only=False)

                return {
                    "continue_workflow": True,
                    "next_request": read_result_step_name,
                    "test_context": test_context
                }

        def read_calculation_result(test_context):
            calculation_id = test_context["calculation_id"]
            result_response = self.bpm_optimizer_api.get_optimization_result(id=calculation_id,
                                                                            _return_http_data_only=False)
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
