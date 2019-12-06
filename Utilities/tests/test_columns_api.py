import unittest

from fds.analyticsapi.engines.api.columns_api import ColumnsApi
from fds.analyticsapi.engines.models.column import Column
from fds.analyticsapi.engines.models.column_summary import ColumnSummary

from common_functions import CommonFunctions

class TestColumnsApi(unittest.TestCase):

    def setUp(self):
        self.columns_api = ColumnsApi(CommonFunctions.build_api_client())

    def test_get_all_pa_columns(self):
        response = self.columns_api.get_pa_columns_with_http_info()
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0]), dict, "Response should be of Dictionary type")
        self.assertEqual(type(response[0][list(response[0].keys())[0]]), ColumnSummary, "Response should be of ColumnSummary type")

    def test_get_pa_column_details_by_id(self):
        columns = self.columns_api.get_pa_columns()
        column_id = list(columns.keys())[0]
        response = self.columns_api.get_pa_column_by_id_with_http_info(column_id)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0]), Column, "Response should be of Column type")

if __name__ == '__main__':
    unittest.main()
