import unittest
import time

from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.model.component_summary import ComponentSummary
from fds.analyticsapi.engines.api.pa_calculations_api import PACalculationsApi
from fds.analyticsapi.engines.model.pa_calculation_parameters import PACalculationParameters
from fds.analyticsapi.engines.model.pa_calculation_parameters_root import PACalculationParametersRoot
from fds.analyticsapi.engines.model.pa_identifier import PAIdentifier
from fds.analyticsapi.engines.model.pa_date_parameters import PADateParameters

from common_functions import CommonFunctions


class TestPaCalculationsApi(unittest.TestCase):
    def setUp(self):
        api_client = CommonFunctions.build_api_client()
        self.pa_calculations_api = PACalculationsApi(api_client)
        self.components_api = ComponentsApi(api_client)

    def test_single_unit_scenario(self):
        create_step_name = "create_calculation"
        read_status_step_name = "read_status"
        read_result_step_name = "read_result"

        def create_calculation(test_context):
            print("Creating single unit calculation")
            components = self.components_api.get_pa_components(document="PA_DOCUMENTS:DEFAULT")
            component_summary = ComponentSummary(name="Weights", category="Weights / Exposures")
            component_id = [id for id in list(components.data.keys()) if components.data[id] == component_summary][0]
            pa_accounts = [PAIdentifier(id="BENCH:SP50")]
            pa_benchmarks = [PAIdentifier(id="BENCH:R.1000")]
            pa_dates = PADateParameters(startdate="20180101", enddate="20181231", frequency="Monthly")

            pa_calculation_parameters = {"1": PACalculationParameters(componentid=component_id, accounts=pa_accounts,
                                                                      benchmarks=pa_benchmarks, dates=pa_dates)}

            pa_calculation_parameter_root = PACalculationParametersRoot(data=pa_calculation_parameters)

            post_and_calculate_response = self.pa_calculations_api.post_and_calculate(
                pa_calculation_parameters_root=pa_calculation_parameter_root, _return_http_data_only=False)

            self.assertTrue(post_and_calculate_response[1] == 201 or post_and_calculate_response[1] == 202,
                            "Response for create_calculation should have been 201 or 202")

            if post_and_calculate_response[1] == 201:
                return {
                    "continue_workflow": False,
                    "next_request": None,
                    "test_context": None
                }
            elif post_and_calculate_response[1] == 202:
                test_context["calculation_id"] = post_and_calculate_response[0].data.calculationid
                return {
                    "continue_workflow": True,
                    "next_request": read_status_step_name,
                    "test_context": test_context
                }

        def read_calculation_status(test_context):
            print("Reading single unit calculation status")
            calculation_id = test_context["calculation_id"]
            print("Calculation Id: " + calculation_id)

            status_response = self.pa_calculations_api.get_calculation_status_by_id(id=calculation_id,
                                                                               _return_http_data_only=False)

            self.assertTrue(status_response[1] == 202 and (status_response[0].data.status in ("Queued", "Executing")))

            while status_response[1] == 202 and (status_response[0].data.status in ("Queued", "Executing")):
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = self.pa_calculations_api.get_calculation_status_by_id(id=calculation_id,
                                                                                   _return_http_data_only=False)

                test_context["calculation_units"] = status_response[0].data.units.items()[0]
                return {
                    "continue_workflow": True,
                    "next_request": read_result_step_name,
                    "test_context": test_context
                }

        def read_calculation_unit_result(test_context):
            calculation_id = test_context["calculation_id"]
            for (calculation_unit_id, calculation_unit) in test_context.calculation_units:
                result_response = self.pa_calculations_api.get_calculation_unit_result_by_id(id=calculation_id,
                                                                                             unit_id=calculation_unit_id,
                                                                                             _return_http_data_only=False)
                self.assertEqual(result_response[1], 200, "Get calculation result should have succeeded")

        workflow_specification = {
            create_step_name: create_calculation,
            read_status_step_name: read_calculation_status,
            read_result_step_name: read_calculation_unit_result
        }
        starting_request = workflow_specification['create_calculation']
        test_context = {}
        run_api_workflow_with_assertions(workflow_specification, starting_request, test_context)


def run_api_workflow_with_assertions(workflow_specification, current_request, test_context):
    current_request_result = current_request(test_context)
    if current_request_result["continue_workflow"]:
        run_api_workflow_with_assertions(
            workflow_specification,
            current_request_result["next_request"],
            current_request_result.test_context
        )


if __name__ == '__main__':
    unittest.main(failfast=True)
