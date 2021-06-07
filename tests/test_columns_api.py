import unittest

from fds.analyticsapi.engines.api.columns_api import ColumnsApi
from fds.analyticsapi.engines.model.column import Column
from fds.analyticsapi.engines.model.column_summary import ColumnSummary

from common_functions import CommonFunctions


class TestColumnsApi(unittest.TestCase):

    def setUp(self):
        self.columns_api = ColumnsApi(CommonFunctions.build_api_client())

    def test_get_all_pa_columns(self):
        response = self.columns_api.get_pa_columns(_return_http_data_only=False)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0]['data']), dict, "Response should be of Dictionary type")
        self.assertEqual(type(response[0]['data'][list(response[0]['data'].keys())[0]]), ColumnSummary, "Response should be of ColumnSummary type")

    def test_get_pa_column_details_by_id(self):
        columns = self.columns_api.get_pa_columns()
        column_id = list(columns.data.keys())[0]
        response = self.columns_api.get_pa_column_by_id(column_id, _return_http_data_only=False)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0]['data']), Column, "Response should be of Column type")


if __name__ == '__main__':
    unittest.main()
