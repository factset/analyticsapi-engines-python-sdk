import unittest

from fds.analyticsapi.engines.api.currencies_api import CurrenciesApi
from fds.analyticsapi.engines.models.currency import Currency

from common_functions import CommonFunctions

class TestCurrenciesApi(unittest.TestCase):

    def setUp(self):
        self.currencies_api = CurrenciesApi(CommonFunctions.build_api_client())

    def test_get_all_currencies(self):
        response = self.currencies_api.get_pa_currencies_with_http_info()
        currency_code = list(response[0].keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), dict, "Response should be of Dictionary type.")
        self.assertEqual(type(response[0][currency_code]), Currency, "Response should be of Currency type.")
        self.assertGreater(len(response[0]), 0, "Response result should not be an empty list.")

if __name__ == '__main__':
    unittest.main()
