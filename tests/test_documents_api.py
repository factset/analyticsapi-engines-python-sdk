import unittest

from fds.analyticsapi.engines.api.documents_api import DocumentsApi
from fds.analyticsapi.engines.model.document_directories import DocumentDirectories

import common_parameters
from common_functions import CommonFunctions

class TestDocumentsApi(unittest.TestCase):

    def setUp(self):
        self.documents_api = DocumentsApi(CommonFunctions.build_api_client())

    def test_get_pa_document_list(self):
        response = self.documents_api.get_pa3_documents(common_parameters.default_lookup_directory, _return_http_data_only=False)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0].data), DocumentDirectories, "Response should be of DocumentDirectories type")

    def test_get_spar_document_list(self):
        response = self.documents_api.get_spar3_documents(common_parameters.default_lookup_directory, _return_http_data_only=False)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0].data), DocumentDirectories, "Response should be of DocumentDirectories type")

    def test_get_vault_document_list(self):
        response = self.documents_api.get_vault_documents(common_parameters.default_lookup_directory, _return_http_data_only=False)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0].data), DocumentDirectories, "Response should be of DocumentDirectories type")

    def test_get_pub_document_list(self):
        response = self.documents_api.get_pub_documents(common_parameters.default_lookup_directory, _return_http_data_only=False)
        self.assertEqual(response[1], 200, "Response code should be 200 - Success")
        self.assertEqual(type(response[0].data), DocumentDirectories, "Response should be of DocumentDirectories type")

if __name__ == '__main__':
    unittest.main()
