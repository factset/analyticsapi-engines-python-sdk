import unittest

from fds.analyticsapi.engines.api.groups_api import GroupsApi
from fds.analyticsapi.engines.model.group import Group
from fds.analyticsapi.engines.model.frequency import Frequency

from common_functions import CommonFunctions


class TestGroupsApi(unittest.TestCase):

    def setUp(self):
        self.groups_api = GroupsApi(CommonFunctions.build_api_client())

    def test_get_all_groups(self):
        response = self.groups_api.get_pa_groups(_return_http_data_only=False)
        group_id = list(response[0].data.keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0].data), dict,
                         "Response should be of dictionary type")
        self.assertEqual(
            type(response[0].data[group_id]), Group, "Response should be of Group type")

    def test_get_pa_grouping_frequencies(self):
        response = self.groups_api.get_pa_grouping_frequencies(_return_http_data_only=False)
        group_frequency_id = list(response[0].data.keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0].data), dict,
                         "Response should be of dictionary type")
        self.assertEqual(
            type(response[0].data[group_frequency_id]), Frequency, "Response should be of Frequency type")


if __name__ == '__main__':
    unittest.main()
