import time
import json
import unittest

from google.protobuf import json_format
from fds.protobuf.stach.Package_pb2 import Package
from urllib3.response import HTTPResponse

from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.api.configurations_api import ConfigurationsApi
from fds.analyticsapi.engines.api.calculations_api import CalculationsApi
from fds.analyticsapi.engines.api.utility_api import UtilityApi
from fds.analyticsapi.engines.models.calculation import Calculation
from fds.analyticsapi.engines.models.pa_calculation_parameters import PACalculationParameters
from fds.analyticsapi.engines.models.pa_identifier import PAIdentifier
from fds.analyticsapi.engines.models.pa_date_parameters import PADateParameters
from fds.analyticsapi.engines.models.spar_calculation_parameters import SPARCalculationParameters
from fds.analyticsapi.engines.models.spar_identifier import SPARIdentifier
from fds.analyticsapi.engines.models.spar_date_parameters import SPARDateParameters
from fds.analyticsapi.engines.models.vault_calculation_parameters import VaultCalculationParameters
from fds.analyticsapi.engines.models.vault_identifier import VaultIdentifier
from fds.analyticsapi.engines.models.vault_date_parameters import VaultDateParameters
from fds.analyticsapi.engines.models.pub_calculation_parameters import PubCalculationParameters
from fds.analyticsapi.engines.models.pub_identifier import PubIdentifier
from fds.analyticsapi.engines.models.pub_date_parameters import PubDateParameters
from fds.analyticsapi.engines.models.calculation_status import CalculationStatus
from fds.analyticsapi.engines.models.calculation_unit_status import CalculationUnitStatus
from fds.analyticsapi.engines.models.calculation_status_summary import CalculationStatusSummary

import common_parameters
from common_functions import CommonFunctions

class TestCalculationsApi(unittest.TestCase):

    def setUp(self):
        self.api_client = CommonFunctions.build_api_client()
        self.calculations_api = CalculationsApi(self.api_client)
        self.create_response = self.run_calculation()
        self.status_response = None

    def run_calculation(self):
        components_api = ComponentsApi(self.api_client)
        components = components_api.get_pa_components(common_parameters.pa_default_document)
        component_id = list(components.keys())[0]

        pa_account_identifier = PAIdentifier(common_parameters.pa_benchmark_sp500)
        pa_accounts = [pa_account_identifier]
        pa_benchmark_identifier = PAIdentifier(common_parameters.pa_benchmark_r1000)
        pa_benchmarks = [pa_benchmark_identifier]
        pa_dates = PADateParameters(common_parameters.default_start_date,
                                    common_parameters.default_end_date,
                                    common_parameters.default_dates_frequency)

        pa_calculation_parameters = {"1": PACalculationParameters(component_id, pa_accounts, pa_benchmarks, pa_dates)}

        components = components_api.get_spar_components(common_parameters.spar_default_document)
        component_id = list(components.keys())[0]

        spar_account_identifier = SPARIdentifier(common_parameters.spar_benchmark_r1000,
                                                 common_parameters.spar_benchmark_russell_return_type,
                                                 common_parameters.spar_benchmark_russell_prefix)
        spar_accounts = [spar_account_identifier]
        spar_benchmark_identifier = SPARIdentifier(common_parameters.spar_benchmark_r2000,
                                                   common_parameters.spar_benchmark_russell_return_type,
                                                   common_parameters.spar_benchmark_russell_prefix)
        spar_dates = SPARDateParameters(common_parameters.default_start_date,
                                        common_parameters.default_end_date,
                                        common_parameters.default_dates_frequency)

        spar_calculation_parameters = {"2": SPARCalculationParameters(component_id, spar_accounts, spar_benchmark_identifier, spar_dates)}

        components = components_api.get_vault_components(common_parameters.vault_default_document)
        component_id = list(components.keys())[0]

        vault_account_identifier = VaultIdentifier(common_parameters.vault_default_account)
        vault_dates = VaultDateParameters(common_parameters.vault_start_date, common_parameters.vault_end_date, common_parameters.default_dates_frequency)

        configurations_api = ConfigurationsApi(self.api_client)
        configurations = configurations_api.get_vault_configurations(common_parameters.vault_default_account)
        configuration_id = list(configurations.keys())[0]

        vault_calculation_parameters = {"3": VaultCalculationParameters(component_id, vault_account_identifier, vault_dates, configuration_id)}

        pub_account_identifier = PubIdentifier(common_parameters.pub_account_name);
        pub_dates = PubDateParameters(common_parameters.pub_start_date, common_parameters.pub_end_date);

        pub_calculation_parameters = {"4": PubCalculationParameters(common_parameters.pub_document_name, pub_account_identifier, pub_dates)}

        calculation = Calculation(pa_calculation_parameters, spar_calculation_parameters, vault_calculation_parameters, pub_calculation_parameters)
        return self.calculations_api.run_calculation_with_http_info(calculation=calculation)

    def test_create_calculation(self):
        self.assertEqual(self.create_response[1], 202, "Response should be 202 - Accepted")
        self.assertEqual(self.create_response[0], None, "Response data should be null.")

    def test_get_calculation_status(self):
        calculation_id = self.create_response[2].get("location").split("/")[-1]
        self.status_response = self.calculations_api.get_calculation_status_by_id_with_http_info(calculation_id)
        self.assertEqual(self.status_response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(self.status_response[0]), CalculationStatus, "Response should be of CalculationStatus type")
        self.assertEqual(type(self.status_response[0].pa), dict, "Response should be of dictionary type")

    def test_calculation_success(self):
        calculation_id = self.create_response[2].get("location").split("/")[-1]
        self.status_response = self.calculations_api.get_calculation_status_by_id_with_http_info(calculation_id)
        while (self.status_response[1] == 200 and (self.status_response[0].status == "Queued" or self.status_response[0].status == "Executing")):
            age_value = self.status_response[2].get("cache-control")
            if age_value is not None:
                max_age = age_value.replace("max-age=", "")
                time.sleep(int(max_age))
            else:
                time.sleep(5)
            self.status_response = self.calculations_api.get_calculation_status_by_id_with_http_info(calculation_id)

        self.assertEqual(self.status_response[1], 200, "Calculation should be completed")
        self.assertEqual(self.status_response[0].status, "Completed", "Calculation status should be completed")
        self.assertEqual(type(self.status_response[0]), CalculationStatus, "Response should be of CalculationStatus type")

        engines = ["pa", "spar", "vault", "pub"]

        for engine in engines:
            calculations = getattr(self.status_response[0], engine).values()
            for calc in calculations:
                self.assertEqual(type(calc), CalculationUnitStatus, "Response should be of CalculationUnitStatus type")
                self.assertEqual(calc.status, "Success", "Calculation should be successful")
                self.assertNotEqual(calc.result, None, "Response result should not be null")

                utility_api = UtilityApi(self.api_client)

                if engine is not "pub":
                    result_response = utility_api.get_by_url_with_http_info(calc.result)
                    result = json_format.Parse(json.dumps(result_response[0]), Package())

                    self.assertEqual(result_response[1], 200, "Response should be 200 - Success")
                    self.assertEqual(type(result), Package, "Response should be of Package type.")
                else:
                    result_response = utility_api.get_by_url_with_http_info(calc.result, _preload_content=False)

                    self.assertEqual(result_response[1], 200, "Response should be 200 - Success")
                    self.assertEqual(type(result_response[0]), HTTPResponse, "Response should be of HTTPResponse type.")

    def test_delete_calculation(self):
        calculation_id = self.create_response[2].get("location").split("/")[-1]
        response = self.calculations_api.cancel_calculation_by_id_with_http_info(calculation_id)
        self.assertEqual(response[1], 204, "Response should be 204 - Success")
        self.assertEqual(response[0], None, "Response data should be null")

    def test_get_all_outstanding_calculations(self):
        response = self.calculations_api.get_calculation_status_summaries_with_http_info()
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), dict, "Response should be of dictionary type")
        first_key = list(response[0].keys())[0]
        self.assertEqual(type(response[0][first_key]), CalculationStatusSummary, "Response should be of CalculationStatusSummary type")

if __name__ == '__main__':
    unittest.main()
