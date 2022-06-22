import unittest
import time

from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.model.component_summary import ComponentSummary
from fds.analyticsapi.engines.api.spar_calculations_api import SPARCalculationsApi
from fds.analyticsapi.engines.model.spar_calculation_parameters import SPARCalculationParameters
from fds.analyticsapi.engines.model.spar_calculation_parameters_root import SPARCalculationParametersRoot
from fds.analyticsapi.engines.model.spar_identifier import SPARIdentifier
from fds.analyticsapi.engines.model.spar_date_parameters import SPARDateParameters

from common_functions import CommonFunctions
from api_workflow import run_api_workflow_with_assertions


class TestSparCalculationsApi(unittest.TestCase):
    def setUp(self):
        api_client = CommonFunctions.build_api_client()
        self.spar_calculations_api = SPARCalculationsApi(api_client)
        self.components_api = ComponentsApi(api_client)
        self.page_number = 1

    def test_single_unit_scenario(self):
        create_step_name = "create_calculation"
        read_status_step_name = "read_status"
        read_result_step_name = "read_result"

        def create_calculation(test_context):
            print("Creating single unit calculation")
            components = self.components_api.get_spar_components(
                document="SPAR_DOCUMENTS:/Factset Default Document",
                _return_http_data_only=True)
            component_summary = ComponentSummary(
                name="Returns Table", category="Raw Data / Returns")
            component_id = [id for id in list(
                components.data.keys()) if components.data[id] == component_summary][0]
            spar_accounts = [SPARIdentifier(id="R.1000")]
            spar_benchmarks = SPARIdentifier(id="RUSSELL_P:R.2000")
            spar_dates = SPARDateParameters(
                startdate="20180101", enddate="20181231", frequency="Monthly")

            spar_calculation_parameters = {"1": SPARCalculationParameters(componentid=component_id, accounts=spar_accounts,
                                                                          benchmark=spar_benchmarks, dates=spar_dates)}

            spar_calculation_parameter_root = SPARCalculationParametersRoot(
                data=spar_calculation_parameters)

            post_and_calculate_response = self.spar_calculations_api.post_and_calculate(
                spar_calculation_parameters_root=spar_calculation_parameter_root,
                cache_control='max-stale=0'
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

            status_response = self.spar_calculations_api.get_calculation_status_by_id(id=calculation_id)

            self.assertTrue(status_response[1] == 202 and (
                status_response[0].data.status in ("Queued", "Executing")))

            while status_response[1] == 202 and (status_response[0].data.status in ("Queued", "Executing")):
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = self.spar_calculations_api.get_calculation_status_by_id(id=calculation_id)

                test_context["calculation_units"] = status_response[0].data.units.items()

            return {
                "continue_workflow": True,
                "next_request": read_result_step_name,
                "test_context": test_context
            }

        def read_calculation_unit_result(test_context):
            calculation_id = test_context["calculation_id"]
            for (calculation_unit_id, calculation_unit) in test_context["calculation_units"]:
                result_response = self.spar_calculations_api.get_calculation_unit_result_by_id(id=calculation_id,
                                                                                               unit_id=calculation_unit_id)
                self.assertEqual(
                    result_response[1], 200, "Get calculation result should have succeeded")

        workflow_specification = {
            create_step_name: create_calculation,
            read_status_step_name: read_calculation_status,
            read_result_step_name: read_calculation_unit_result
        }
        starting_request = workflow_specification['create_calculation']
        test_context = {}
        run_api_workflow_with_assertions(
            workflow_specification, starting_request, test_context)

    def test_get_all_calculations_scenario(self):
        response = self.spar_calculations_api.get_all_calculations(page_number=self.page_number)
        self.assertEqual(response[1], 200, "Response should be 200 - Success")


if __name__ == '__main__':
    unittest.main(failfast=True)
