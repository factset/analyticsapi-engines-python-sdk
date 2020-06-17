import unittest

from fds.analyticsapi.engines.api.documents_api import DocumentsApi
from fds.analyticsapi.engines.models.document_directories import DocumentDirectories

import common_parameters
from common_functions import CommonFunctions

class TestDocumentsApi(unittest.TestCase):

    def setUp(self):
        self.documents_api = DocumentsApi(CommonFunctions.build_api_client())

    def test_get_pa_document_list(self):
        response = self.documents_api.get_pa3_documents_with_http_info(common_parameters.default_lookup_directory)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0]), DocumentDirectories, "Response should be of DocumentDirectories type")

    def test_get_spar_document_list(self):
        response = self.documents_api.get_spar3_documents_with_http_info(common_parameters.default_lookup_directory)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0]), DocumentDirectories, "Response should be of DocumentDirectories type")

    def test_get_vault_document_list(self):
        response = self.documents_api.get_vault_documents_with_http_info(common_parameters.default_lookup_directory)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0]), DocumentDirectories, "Response should be of DocumentDirectories type")

    def test_get_pub_document_list(self):
        response = self.documents_api.get_pub_documents_with_http_info(common_parameters.default_lookup_directory)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0]), DocumentDirectories, "Response should be of DocumentDirectories type")

if __name__ == '__main__':
    unittest.main()
