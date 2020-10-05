import unittest

from fds.analyticsapi.engines.api.frequencies_api import FrequenciesApi
from fds.analyticsapi.engines.models.frequency import Frequency

from common_functions import CommonFunctions

class TestFrequenciesApi(unittest.TestCase):

    def setUp(self):
        self.frequencies_api = FrequenciesApi(CommonFunctions.build_api_client())

    def test_get_pa_frequencies(self):
        response = self.frequencies_api.get_pa_frequencies_with_http_info()
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), dict, "Response should be of dictionary type.")
        frequencies = list(response[0].keys())
        first_key = frequencies[0]
        self.assertEqual(type(response[0][first_key]), Frequency, "Response should be of Frequency type.")
        self.assertGreater(len(frequencies), 0, "Response result should not be an empty list.")

    def test_get_spar_frequencies(self):
        response = self.frequencies_api.get_spar_frequencies_with_http_info()
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), dict, "Response should be of dictionary type.")
        frequencies = list(response[0].keys())
        first_key = frequencies[0]
        self.assertEqual(type(response[0][first_key]), Frequency, "Response should be of Frequency type.")
        self.assertGreater(len(frequencies), 0, "Response result should not be an empty list.")

    def test_get_vault_frequencies(self):
        response = self.frequencies_api.get_vault_frequencies_with_http_info()
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), dict, "Response should be of dictionary type.")
        frequencies = list(response[0].keys())
        first_key = frequencies[0]
        self.assertEqual(type(response[0][first_key]), Frequency, "Response should be of Frequency type.")
        self.assertGreater(len(frequencies), 0, "Response result should not be an empty list.")

if __name__ == '__main__':
    unittest.main()
