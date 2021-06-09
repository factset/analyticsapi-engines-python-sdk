import unittest
import time
import json

from google.protobuf import json_format
from fds.protobuf.stach.Package_pb2 import Package
from urllib3.response import HTTPResponse

from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.api.configurations_api import ConfigurationsApi
from fds.analyticsapi.engines.model.pa_calculation_parameters import PACalculationParameters
from fds.analyticsapi.engines.model.pa_identifier import PAIdentifier
from fds.analyticsapi.engines.model.pa_date_parameters import PADateParameters
from fds.analyticsapi.engines.model.spar_calculation_parameters import SPARCalculationParameters
from fds.analyticsapi.engines.model.spar_identifier import SPARIdentifier
from fds.analyticsapi.engines.model.spar_date_parameters import SPARDateParameters
from fds.analyticsapi.engines.model.vault_calculation_parameters import VaultCalculationParameters
from fds.analyticsapi.engines.model.vault_identifier import VaultIdentifier
from fds.analyticsapi.engines.model.vault_date_parameters import VaultDateParameters
from fds.analyticsapi.engines.model.pub_calculation_parameters import PubCalculationParameters
from fds.analyticsapi.engines.model.pub_identifier import PubIdentifier
from fds.analyticsapi.engines.model.pub_date_parameters import PubDateParameters
from fds.analyticsapi.engines.model.calculation_status import CalculationStatus
from fds.analyticsapi.engines.model.calculation_unit_status import CalculationUnitStatus
from fds.analyticsapi.engines.model.calculation_status_summary import CalculationStatusSummary


import common_parameters
from common_functions import CommonFunctions


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
