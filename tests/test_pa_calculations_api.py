import unittest
import time
import json

from google.protobuf import json_format
from fds.protobuf.stach.Package_pb2 import Package
from urllib3.response import HTTPResponse

from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.api.pa_calculations_api import PACalculationsApi
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

import common_parameters
from common_functions import CommonFunctions


class TestPaCalculationsApi(unittest.TestCase):
    def setUp(self):
        self.calculations_api = PACalculationsApi(CommonFunctions.build_api_client())

    def test_single_unit_scenario(self):
        workflow_specification = {}
        starting_request = workflow_specification['create_calculation']
        environment = {}
        self.run_api_workflow_with_assertions(workflow_specification, starting_request, environment)

    def test_multiple_unit_scenario(self):
        workflow_specification = {}
        starting_request = workflow_specification['create_calculation']
        environment = {}
        self.run_api_workflow_with_assertions(workflow_specification, starting_request, environment)

    def run_api_workflow_with_assertions(self, workflow_specification, current_request, environment):
        print("something")


if __name__ == '__main__':
    unittest.main()
