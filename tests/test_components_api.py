import unittest

from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.model.component_summary import ComponentSummary
from fds.analyticsapi.engines.model.pa_component import PAComponent
from fds.analyticsapi.engines.model.pa_component_root import PAComponentRoot
from fds.analyticsapi.engines.model.component_summary_root import ComponentSummaryRoot
from fds.analyticsapi.engines.model.vault_component import VaultComponent

import common_parameters
from common_functions import CommonFunctions


class TestComponentsApi(unittest.TestCase):

    def setUp(self):
        self.components_api = ComponentsApi(CommonFunctions.build_api_client())

    ######################################################################################
                                   # PA Components Test Cases
    ######################################################################################

    def test_get_all_pa_components(self):
        response = self.components_api.get_pa_components(
            document=common_parameters.pa_default_document,
            _return_http_data_only=False
        )
        component_id = list(response[0]['data'].keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), ComponentSummaryRoot, "Response should be of dictionary type")
        self.assertEqual(type(response[0]['data'][component_id]), ComponentSummary, "Response should be of ComponentSummary type")

    # This test encounters ApiTypeException due to response having fields set to null instead of being hidden
    @unittest.skip("Skip until fix API behavior where null property is returned instead of hidden")
    def test_get_pa_component_by_id(self):
        components = self.components_api.get_pa_components(document=common_parameters.pa_default_document)
        component_id = list(components['data'].keys())[0]
        response = self.components_api.get_pa_component_by_id(id=component_id, _return_http_data_only=False)
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), PAComponentRoot, "Response should be of PAComponentRoot type.")

    ######################################################################################
                                   # Vault Components Test Cases
    ######################################################################################

    def test_get_all_vault_components(self):
        response = self.components_api.get_vault_components(
            document=common_parameters.vault_default_document,
            _return_http_data_only=False
        )
        component_id = list(response[0]['data'].keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), ComponentSummaryRoot, "Response should be of dictionary type")
        self.assertEqual(type(response[0]['data'][component_id]), ComponentSummary, "Response should be of ComponentSummary type")

    # This test encounters ApiTypeException due to response having fields set to null instead of being hidden
    @unittest.skip("Skip until fix API behavior where null property is returned instead of hidden")
    def test_get_vault_component_by_id(self):
        components = self.components_api.get_vault_components(document=common_parameters.vault_default_document)
        component_id = list(components['data'].keys())[0]
        response = self.components_api.get_vault_component_by_id(component_id, _return_http_data_only=False)
        component_id = list(response[0]['data'].keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]['data']), VaultComponent, "Response should be of VaultComponent type.")

    ######################################################################################
                                   # Spar Components Test Cases
    ######################################################################################

    def test_get_all_spar_components(self):
        response = self.components_api.get_spar_components(
            document=common_parameters.spar_default_document,
            _return_http_data_only=False
        )
        component_id = list(response[0]['data'].keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), ComponentSummaryRoot, "Response should be of dictionary type")
        self.assertEqual(type(response[0]['data'][component_id]), ComponentSummary, "Response should be of ComponentSummary type")


if __name__ == '__main__':
    unittest.main()
