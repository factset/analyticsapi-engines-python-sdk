import unittest

from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.models.component_summary import ComponentSummary
from fds.analyticsapi.engines.models.pa_component import PAComponent
from fds.analyticsapi.engines.models.vault_component import VaultComponent

import common_parameters
from common_functions import CommonFunctions

class TestComponentsApi(unittest.TestCase):

    def setUp(self):
        self.components_api = ComponentsApi(CommonFunctions.build_api_client())

    ######################################################################################
                                   # PA Components Test Cases
    ######################################################################################

    def test_get_all_pa_components(self):
        response = self.components_api.get_pa_components_with_http_info(document=common_parameters.pa_default_document)
        component_id = list(response[0].keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), dict, "Response should be of dictionary type")
        self.assertEqual(type(response[0][component_id]), ComponentSummary, "Response should be of ComponentSummary type")

    def test_get_pa_component_by_id(self):
        components = self.components_api.get_pa_components(document=common_parameters.pa_default_document)
        component_id = list(components.keys())[0]
        response = self.components_api.get_pa_component_by_id_with_http_info(component_id)
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), PAComponent, "Response should be of PAComponent type.")


    ######################################################################################
                                   # Vault Components Test Cases
    ######################################################################################

    def test_get_all_vault_components(self):
        response = self.components_api.get_vault_components_with_http_info(document=common_parameters.vault_default_document)
        component_id = list(response[0].keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), dict, "Response should be of dictionary type")
        self.assertEqual(type(response[0][component_id]), ComponentSummary, "Response should be of ComponentSummary type")

    def test_get_vault_component_by_id(self):
        components = self.components_api.get_vault_components(document=common_parameters.vault_default_document)
        component_id = list(components.keys())[0]
        response = self.components_api.get_vault_component_by_id_with_http_info(component_id)
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), VaultComponent, "Response should be of VaultComponent type.")


    ######################################################################################
                                   # Spar Components Test Cases
    ######################################################################################

    def test_get_all_spar_components(self):
        response = self.components_api.get_spar_components_with_http_info(document=common_parameters.spar_default_document)
        component_id = list(response[0].keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), dict, "Response should be of dictionary type")
        self.assertEqual(type(response[0][component_id]), ComponentSummary, "Response should be of ComponentSummary type")

if __name__ == '__main__':
    unittest.main()
