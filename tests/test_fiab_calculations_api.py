import unittest
import time

from fds.analyticsapi.engines.api.fiab_calculations_api import FIABCalculationsApi
from fds.analyticsapi.engines.model.fiab_calculation_parameters import FIABCalculationParameters
from fds.analyticsapi.engines.model.fiab_identifier import FIABIdentifier
from fds.analyticsapi.engines.model.fiab_date_parameters import FIABDateParameters

from common_functions import CommonFunctions
from api_workflow import run_api_workflow_with_assertions


class TestFiabCalculationsApi(unittest.TestCase):
    def setUp(self):
        api_client = CommonFunctions.build_api_client()
        self.fiab_calculations_api = FIABCalculationsApi(api_client)

    @unittest.skip("Skip until can fix the QA user workflow")
    def test_single_unit_scenario(self):
        create_step_name = "create_calculation"
        read_status_step_name = "read_status"
        read_result_step_name = "read_result"

        def create_calculation(test_context):
            print("Creating single unit calculation")
            fiab_document = "Client:/aapi/AAPI_FIAB_BASE_DOC"
            fiab_account = FIABIdentifier(
                id="Client:/aapi/FIAB_TEST_HOLDINGS.ACCT")
            fiab_msl = "CLIENT:$$MSL_AAPI_TESTING.OFDB"
            fiab_dates = FIABDateParameters(
                startdate="20200618", enddate="20200618")

            fiab_calculation_parameters = FIABCalculationParameters(account=fiab_account, dates=fiab_dates,
                                                                    fiabdocument=fiab_document, msl=fiab_msl)

            post_and_calculate_response = self.fiab_calculations_api.run_calculation(
                fiab_calculation_parameters=fiab_calculation_parameters, _return_http_data_only=False)

            self.assertTrue(post_and_calculate_response[1] == 202,
                            "Response for create_calculation should have been 202")

            if post_and_calculate_response[1] == 202:
                test_context["calculation_id"] = post_and_calculate_response[2]["x-factset-api-calculation-id"]
                return {
                    "continue_workflow": True,
                    "next_request": read_status_step_name,
                    "test_context": test_context
                }

        def read_calculation_status(test_context):
            print("Reading single unit calculation status")
            calculation_id = test_context["calculation_id"]
            print("Calculation Id: " + calculation_id)

            status_response = self.fiab_calculations_api.get_calculation_by_id(id=calculation_id,
                                                                               _return_http_data_only=False)

            self.assertTrue(status_response[1] == 202 and (
                status_response[0].status in ("Pending", "InProgress", "Done")))

            while status_response[1] == 202 and (status_response[0].status in ("Pending", "InProgress")):
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = self.fiab_calculations_api.get_calculation_by_id(id=calculation_id,
                                                                                   _return_http_data_only=False)
            return {
                "continue_workflow": True,
                "next_request": read_result_step_name,
                "test_context": test_context
            }

        def read_calculation_result(test_context):
            calculation_id = test_context["calculation_id"]
            status_response = self.fiab_calculations_api.get_calculation_by_id(id=calculation_id,
                                                                               _return_http_data_only=False)
            self.assertEqual(
                status_response[1], 200, "Get calculation result should have succeeded")
            self.assertTrue(status_response[0].status == "Done",
                            "Get calculation result should have Done status")

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
