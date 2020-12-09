import unittest

from fds.analyticsapi.engines.api.strategy_documents_api import StrategyDocumentsApi
from fds.analyticsapi.engines.models.document_directories import DocumentDirectories

import common_parameters
from common_functions import CommonFunctions

class TestStrategyDocuments(unittest.TestCase):

    def setUp(self):
        self.strategy_document_api = StrategyDocumentsApi(CommonFunctions.build_api_client())

    def test_get_directories(self):
        response = self.strategy_document_api.get_axioma_equity_strategy_documents(common_parameters.default_lookup_directory)
        self.assertEqual(type(response), DocumentDirectories, "Response should be of DocumentDirectories type")



if __name__ == '__main__':
    unittest.main()
