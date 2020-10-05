import unittest

from fds.analyticsapi.engines.api.accounts_api import AccountsApi
from fds.analyticsapi.engines.models.account_directories import AccountDirectories

import common_parameters
from common_functions import CommonFunctions

class TestAccountsApi(unittest.TestCase):

    def setUp(self):
        self.accounts_api = AccountsApi(CommonFunctions.build_api_client())

    def test_get_account_list(self):
        response = self.accounts_api.get_accounts_with_http_info(common_parameters.default_lookup_directory)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0]), AccountDirectories, "Response should be of AccountDirectories type")

if __name__ == '__main__':
    unittest.main()
