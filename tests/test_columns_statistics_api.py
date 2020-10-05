import unittest

from fds.analyticsapi.engines.api.column_statistics_api import ColumnStatisticsApi
from fds.analyticsapi.engines.models.column_statistic import ColumnStatistic

from common_functions import CommonFunctions

class TestColumnStatisticsApi(unittest.TestCase):

    def setUp(self):
        self.column_statistics_api = ColumnStatisticsApi(CommonFunctions.build_api_client())

    def test_get_column_statistics(self):
        response = self.column_statistics_api.get_pa_column_statistics_with_http_info()
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0]), dict, "Response should be of Dictionary type")
        self.assertEqual(type(response[0][list(response[0].keys())[0]]), ColumnStatistic, "Response should be of ColumnStatistic type")

if __name__ == '__main__':
    unittest.main()
