import unittest

from fds.analyticsapi.engines.api.discount_curves_api import DiscountCurvesApi
from fds.analyticsapi.engines.model.fi_discount_curve_info_root import FIDiscountCurveInfoRoot

from common_functions import CommonFunctions


class TestDiscountCurvesApi(unittest.TestCase):

    def setUp(self):
        self.discount_curves_api = DiscountCurvesApi(CommonFunctions.build_api_client())

    def test_get_all_discount_curves(self):
        response = self.discount_curves_api.get_all_fi_discount_curves()
        currency_code = list(response[0].data.keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0].data), dict,
                         "Response should be of Dictionary type.")
        self.assertGreater(
            len(response[0].data), 0, "Response result should not be an empty list.")
        
    def test_get_all_discount_curves_currency_usd(self):
        response = self.discount_curves_api.get_all_fi_discount_curves(currency = "INR")
        currency_code = list(response[0].data.keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0].data), dict,
                         "Response should be of Dictionary type.")
        self.assertGreater(
            len(response[0].data), 0, "Response result should not be an empty list.")
        
    def test_get_all_discount_curves_currency_randomvalue(self):
        response = self.discount_curves_api.get_all_fi_discount_curves(currency = "randomValue")
        currency_code = list(response[0].data.keys())[0]
        self.assertEqual(response[1], 404, "Response should be 404 - Not Found")

if __name__ == '__main__':
    unittest.main()
