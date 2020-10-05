import unittest

from fds.analyticsapi.engines.api.configurations_api import ConfigurationsApi
from fds.analyticsapi.engines.models.vault_configuration_summary import VaultConfigurationSummary
from fds.analyticsapi.engines.models.vault_configuration import VaultConfiguration

import common_parameters
from common_functions import CommonFunctions

class TestVaultConfigurations(unittest.TestCase):

    def setUp(self):
        self.configurations_api = ConfigurationsApi(CommonFunctions.build_api_client())

    def test_get_all_vault_configurations(self):
        response = self.configurations_api.get_vault_configurations_with_http_info(account=common_parameters.vault_default_account)
        configuration_id = list(response[0].keys())[0]
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0]), dict, "Response should be of Dictionary type")
        self.assertEqual(type(response[0][configuration_id]), VaultConfigurationSummary, "Response should be of VaultConfigurationSummary type")

    def test_get_vault_configuration_by_id(self):
        configurations = self.configurations_api.get_vault_configurations(account=common_parameters.vault_default_account)
        configuration_id = list(configurations.keys())[0]
        response = self.configurations_api.get_vault_configuration_by_id_with_http_info(configuration_id)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0]), VaultConfiguration, "Response should be of VaultConfiguration type")

if __name__ == '__main__':
    unittest.main()
