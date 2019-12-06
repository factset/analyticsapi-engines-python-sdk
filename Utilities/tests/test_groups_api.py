import unittest

from fds.analyticsapi.engines.api.groups_api import GroupsApi
from fds.analyticsapi.engines.models.group import Group

from common_functions import CommonFunctions

class TestGroupsApi(unittest.TestCase):

    def setUp(self):
        self.groups_api = GroupsApi(CommonFunctions.build_api_client())

    def test_get_all_groups(self):
        response = self.groups_api.get_pa_groups_with_http_info()
        group_id = list(response[0].keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), dict, "Response should be of dictionary type")
        self.assertEqual(type(response[0][group_id]), Group, "Response should be of Group type")

if __name__ == '__main__':
    unittest.main()
