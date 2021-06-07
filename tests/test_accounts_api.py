import unittest

from fds.analyticsapi.engines.api.accounts_api import AccountsApi
from fds.analyticsapi.engines.model.account_directories_root import AccountDirectoriesRoot

import common_parameters
from common_functions import CommonFunctions


class TestAccountsApi(unittest.TestCase):

    def setUp(self):
        self.accounts_api = AccountsApi(CommonFunctions.build_api_client())

    def test_get_account_list(self):
        response = self.accounts_api.get_accounts(common_parameters.default_lookup_directory, _return_http_data_only=False)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0]), AccountDirectoriesRoot, "Response should be of AccountDirectoriesRoot type")


if __name__ == '__main__':
    unittest.main()
