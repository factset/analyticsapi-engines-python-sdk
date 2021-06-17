import unittest

from fds.analyticsapi.engines.api.configurations_api import ConfigurationsApi
from fds.analyticsapi.engines.model.vault_configuration_summary import VaultConfigurationSummary
from fds.analyticsapi.engines.model.vault_configuration import VaultConfiguration

import common_parameters
from common_functions import CommonFunctions


class TestVaultConfigurations(unittest.TestCase):

    def setUp(self):
        self.configurations_api = ConfigurationsApi(
            CommonFunctions.build_api_client())

    def test_get_all_vault_configurations(self):
        response = self.configurations_api.get_vault_configurations(account=common_parameters.vault_default_account,
                                                                    _return_http_data_only=False)
        configuration_id = list(response[0].data.keys())[0]
        self.assertEqual(response[1], 200,
                         "Response code should be 200 - Success")
        self.assertEqual(type(response[0].data), dict,
                         "Response should be of Dictionary type")
        self.assertEqual(type(response[0].data[configuration_id]), VaultConfigurationSummary,
                         "Response should be of VaultConfigurationSummary type")

    def test_get_vault_configuration_by_id(self):
        response = self.configurations_api.get_vault_configurations(
            account=common_parameters.vault_default_account,
            _return_http_data_only=True)
        configuration_id = list(response.data.keys())[0]
        response = self.configurations_api.get_vault_configuration_by_id(configuration_id,
                                                                         _return_http_data_only=False)
        self.assertEqual(response[1], 200,
                         "Response code should be 200 - Success")
        self.assertEqual(type(response[0].data), VaultConfiguration,
                         "Response should be of VaultConfiguration type")


if __name__ == '__main__':
    unittest.main()
