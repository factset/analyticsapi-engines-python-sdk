import unittest

from fds.analyticsapi.engines.api.spar_benchmark_api import SPARBenchmarkApi
from fds.analyticsapi.engines.models.spar_benchmark import SPARBenchmark

import common_parameters
from common_functions import CommonFunctions

class TestSparBenchmarkApi(unittest.TestCase):

    def setUp(self):
        self.spar_benchmark_api = SPARBenchmarkApi(CommonFunctions.build_api_client())

    def test_get_spar_benchmark_by_id(self):
        response = self.spar_benchmark_api.get_spar_benchmark_by_id_with_http_info(common_parameters.spar_benchmark_r1000)
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), SPARBenchmark, "Response should be of SPARBenchmark type")

if __name__ == '__main__':
    unittest.main()
