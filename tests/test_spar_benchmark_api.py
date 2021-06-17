import unittest

from fds.analyticsapi.engines.api.benchmarks_api import BenchmarksApi
from fds.analyticsapi.engines.model.spar_benchmark_root import SPARBenchmarkRoot

import common_parameters
from common_functions import CommonFunctions


class TestSparBenchmarkApi(unittest.TestCase):

    def setUp(self):
        self.spar_benchmark_api = BenchmarksApi(
            CommonFunctions.build_api_client())

    def test_get_spar_benchmark_by_id(self):
        response = self.spar_benchmark_api.get_spar_benchmark_by_id(common_parameters.spar_benchmark_r1000,
                                                                    _return_http_data_only=False
                                                                    )
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(
            type(response[0]), SPARBenchmarkRoot, "Response should be of SPARBenchmark type")


if __name__ == '__main__':
    unittest.main()
