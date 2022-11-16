import unittest
import time

from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.api.configurations_api import ConfigurationsApi
from fds.analyticsapi.engines.api.quant_calculations_api import QuantCalculationsApi
from fds.analyticsapi.engines.model.quant_calculation_parameters import QuantCalculationParameters
from fds.analyticsapi.engines.model.quant_calculation_parameters_root import QuantCalculationParametersRoot
from fds.analyticsapi.engines.model.quant_identifier_universe import QuantIdentifierUniverse
from fds.analyticsapi.engines.model.quant_screening_expression import QuantScreeningExpression
from fds.analyticsapi.engines.model.quant_fql_expression import QuantFqlExpression
from fds.analyticsapi.engines.model.quant_fds_date import QuantFdsDate
from fds.analyticsapi.engines.model.quant_calculation_meta import QuantCalculationMeta
from common_functions import CommonFunctions
from api_workflow import run_api_workflow_with_assertions


class TestQuantCalculationsApi(unittest.TestCase):
    def setUp(self):
        api_client = CommonFunctions.build_api_client()
        self.quant_calculations_api = QuantCalculationsApi(api_client)
        self.configurations_api = ConfigurationsApi(api_client)
        self.components_api = ComponentsApi(api_client)
        self.page_number = 1

    def test_single_unit_scenario(self):
        create_step_name = "create_calculation"
        read_status_step_name = "read_status"
        read_result_step_name = "read_result"

        def create_calculation(test_context):
            print("Creating single unit calculation")

            if(test_context["is_array_return_type"]):
                quant_formulas = [
                QuantScreeningExpression(expr="P_PRICE", name="Price (SCR)", source="ScreeningExpression"),
                (QuantFqlExpression(expr="P_PRICE", name="Price (SCR)", source="FqlExpression")),
                (QuantFqlExpression(expr="P_PRICE(#DATE,#DATE-5D,#FREQ)", name="Price",
                                    is_array_return_type=True, source="FqlExpression"))]
            else:
                quant_formulas = [
                    QuantScreeningExpression(expr="P_PRICE", name="Price (SCR)", source="ScreeningExpression"),
                    (QuantFqlExpression(expr="P_PRICE", name="Price (SCR)", source="FqlExpression"))]

            quant_dates = QuantFdsDate(start_date="0", end_date="-5D", source="FdsDate", frequency="D", calendar="FIVEDAY")

            quant_calculations_meta = QuantCalculationMeta(format="Feather")

            quant_identifiers = ["03748R74", "S8112735"]
            quant_identifier_universe = QuantIdentifierUniverse(universe_type="Equity"
                                                                , identifiers=quant_identifiers
                                                                , source="IdentifierUniverse")

            quant_calculation_parameters = {"1": QuantCalculationParameters(universe=quant_identifier_universe,
                                                                            dates=quant_dates, formulas=quant_formulas)}

            quant_calculation_parameter_root = QuantCalculationParametersRoot(
                data=quant_calculation_parameters, meta=quant_calculations_meta)

            post_and_calculate_response = self.quant_calculations_api.post_and_calculate(
                quant_calculation_parameters_root=quant_calculation_parameter_root
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

            status_response = self.quant_calculations_api.get_calculation_status_by_id(id=calculation_id)

            self.assertTrue(status_response[1] == 202 and (
                status_response[0].data.status in ("Queued", "Executing")))

            while status_response[1] == 202 and (status_response[0].data.status in ("Queued", "Executing")):
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = self.quant_calculations_api.get_calculation_status_by_id(id=calculation_id)

                test_context["calculation_units"] = status_response[0].data.units.items()

            return {
                "continue_workflow": True,
                "next_request": read_result_step_name,
                "test_context": test_context
            }

        def process_calculations_units(test_context):
            calculation_id = test_context["calculation_id"]
            for (calculation_unit_id, calculation_unit) in test_context["calculation_units"]:
                result_response = self.quant_calculations_api.get_calculation_unit_result_by_id(id=calculation_id,
                                                                                                unit_id=calculation_unit_id)
                self.assertEqual(
                    result_response[1], 200, "Get calculation result should have succeeded")

            return {
                "continue_workflow": False,
                "next_request": read_result_step_name,
                "test_context": test_context
            }

        def read_calculation_unit_result_isarrayreturntype(test_context):
            process_calculations_units(test_context)

        workflow_specification = {
            create_step_name: create_calculation,
            read_status_step_name: read_calculation_status,
            read_result_step_name: read_calculation_unit_result_isarrayreturntype
        }
        starting_request = workflow_specification['create_calculation']
        test_context = {}
        test_context["is_array_return_type"] = 'True'
        run_api_workflow_with_assertions(
            workflow_specification, starting_request, test_context)

        def read_calculation_unit_result(test_context):
            process_calculations_units(test_context)

        workflow_specification = {
            create_step_name: create_calculation,
            read_status_step_name: read_calculation_status,
            read_result_step_name: read_calculation_unit_result
        }
        starting_request = workflow_specification['create_calculation']
        test_context = {}
        test_context["is_array_return_type"] = 'False'
        run_api_workflow_with_assertions(
            workflow_specification, starting_request, test_context)

    def test_get_all_calculations_scenario(self):
        response = self.quant_calculations_api.get_all_calculations(page_number=self.page_number)
        self.assertEqual(response[1], 200, "Response should be 200 - Success")


if __name__ == '__main__':
    unittest.main(failfast=True)
