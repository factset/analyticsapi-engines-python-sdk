import time
import json
import unittest
import sys
import uuid

from fds.analyticsapi.engines.api.fi_calculations_api import FICalculationsApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.models.fi_calculation_parameters import FICalculationParameters
from fds.analyticsapi.engines.models.fi_security import FISecurity
from fds.analyticsapi.engines.models.fi_job_settings import FIJobSettings
from fds.analyticsapi.engines.stach_extensions import StachExtensions
from fds.protobuf.stach.Package_pb2 import Package

from google.protobuf import json_format
from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import MessageToDict

import common_parameters
from common_functions import CommonFunctions


class TestFICalculationsApi(unittest.TestCase):
    def setUp(self):
        self.api_client = CommonFunctions.build_api_client()
        self.calculations_api = FICalculationsApi(self.api_client)
        self.run_response = self.run_calculation()
        self.status_response = None

    def run_calculation(self):
        calculations = ["Security Type",
                        "Security Name",
                        "Run Status",
                        "Elapse Time (seconds)",
                        "Calc From Method",
                        "Option Pricing Model",
                        "Yield Curve Date",
                        "Settlement Date",
                        "Discount Curve",
                        "Price",
                        "Yield to No Call",
                        "OAS",
                        "Effective Duration",
                        "Effective Convexity"]

        security1 = FISecurity("Price", 100.285, 10000.0, "912828ZG8", "20201202", "UST")
        security2 = FISecurity("Price", 101.138, 200000.0, "US037833AR12", "20201203", "UST")

        securities = [security1, security2]

        jobSettings = FIJobSettings("20201201")

        fi_calculation_parameters = FICalculationParameters(securities, calculations, jobSettings)
        return self.calculations_api.run_fi_calculation_with_http_info(
            fi_calculation_parameters=fi_calculation_parameters)

    def test_calculation_success(self):
        if self.run_response[1] == 202:
            calculation_id = self.run_response[2].get("location").split("/")[-1]
            self.run_response = self.calculations_api.get_fi_calculation_by_id_with_http_info(calculation_id)
            while self.run_response[1] == 202:
                age_value = self.run_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                    time.sleep(int(max_age))
                else:
                    time.sleep(5)
                self.run_response = self.calculations_api.get_fi_calculation_by_id_with_http_info(calculation_id)

        self.assertTrue(self.run_response[1] == 200 or self.run_response[1] == 201, "Calculation should be completed")


if __name__ == '__main__':
    unittest.main()