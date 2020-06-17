import unittest

from fds.analyticsapi.engines.api.dates_api import DatesApi
from fds.analyticsapi.engines.api.components_api import ComponentsApi

import common_parameters
from common_functions import CommonFunctions

class TestDatesApi(unittest.TestCase):

    def setUp(self):
        self.dates_api = DatesApi(CommonFunctions.build_api_client())

    def test_convert_pa_date_to_absolute_format(self):
        end_date = "-1M"
        # hard coding this as we won't know if the component requires start date
        component_id = "918EE8207D259B54E2FDE2AAA4D3BEA9248164123A904F298B8438B76F9292EB"
        account = common_parameters.default_dates_account
        response = self.dates_api.convert_pa_dates_to_absolute_format_with_http_info(end_date, component_id, account)
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertNotEqual(response[0], None, "Response data should not be null")

    def test_convert_vault_date_to_absolute_format(self):
        end_date = "-1M"
        components_api = ComponentsApi(CommonFunctions.build_api_client())
        components = components_api.get_vault_components(document=common_parameters.vault_default_document)
        component_id = list(components.keys())[0]
        account = common_parameters.default_dates_account
        response = self.dates_api.convert_vault_dates_to_absolute_format_with_http_info(end_date, component_id, account)
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertNotEqual(response[0], None, "Response data should not be null")

if __name__ == '__main__':
    unittest.main()
