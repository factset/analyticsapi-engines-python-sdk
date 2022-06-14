import unittest

from fds.analyticsapi.engines.api.pricing_sources_api import PricingSourcesApi

from common_functions import CommonFunctions


class TestPricingSourcesApi(unittest.TestCase):

    def setUp(self):
        self.pricing_sources_api = PricingSourcesApi(CommonFunctions.build_api_client())

    def test_pricing_sources(self):
        response = self.pricing_sources_api.get_pa_pricing_sources(_return_http_data_only=False)
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0].data), dict,
                         "Response should be of dictionary type")


if __name__ == '__main__':
    unittest.main()
