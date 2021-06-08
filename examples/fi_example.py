import sys
import time
import pandas as pd
import uuid
import os

from fds.analyticsapi.engines.api.fi_calculations_api import FICalculationsApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.fi_calculation_parameters import FICalculationParameters
from fds.analyticsapi.engines.model.fi_calculation_parameters_root import FICalculationParametersRoot
from fds.analyticsapi.engines.model.fi_security import FISecurity
from fds.analyticsapi.engines.model.fi_job_settings import FIJobSettings
from fds.protobuf.stach.extensions.StachVersion import StachVersion
from fds.protobuf.stach.extensions.StachExtensionFactory import StachExtensionFactory

from urllib3 import Retry

host = "https://api.factset.com"
username = os.environ["ANALYTICS_API_USERNAME_SERIAL"]
password = os.environ["ANALYTICS_API_PASSWORD"]


def main():
    config = Configuration()
    config.host = host
    config.username = username
    config.password = password
    # add proxy and/or disable ssl verification according to your development environment
    # config.proxy = "<proxyUrl>"
    config.verify_ssl = False

    # Setting configuration to retry api calls on http status codes of 429 and 503.
    config.retries = Retry(total=3, status=3, status_forcelist=frozenset([429, 503]), backoff_factor=2,
                           raise_on_status=False)

    api_client = ApiClient(config)

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

    securities = [
        FISecurity("Price", 100.285, "912828ZG8", settlement="20201202", discount_curve="UST", face=10000.0),
        FISecurity("Price", 101.138, "US037833AR12", settlement="20201203", discount_curve="UST", face=200000.0)
    ]
    jobSettings = FIJobSettings("20201201")
    fi_calculation_parameters = FICalculationParameters(securities, calculations, jobSettings)
    fi_calculation_parameters_root = FICalculationParametersRoot(data=fi_calculation_parameters)

    print("FI Calculation Parameters Root:")
    print(fi_calculation_parameters_root)

    fi_calculations_api = FICalculationsApi(api_client)
    run_calculation_response = fi_calculations_api.post_and_calculate(
        fi_calculation_parameters_root=fi_calculation_parameters_root,
        _return_http_data_only=False)

    if run_calculation_response[1] != 202 and run_calculation_response[1] != 201:
        print_error(run_calculation_response)
        sys.exit()

    if run_calculation_response[1] == 201:
        output_calculation_result(run_calculation_response[0])
        sys.exit()

    calculation_id = run_calculation_response[0].data.id
    print("Calculation Id: " + calculation_id)

    status_response = fi_calculations_api.get_calculation_status_by_id(id=calculation_id)
    while status_response[1] == 202:
        max_age = '5'
        age_value = status_response[2].get("cache-control")
        if age_value is not None:
            max_age = age_value.replace("max-age=", "")
        print('Sleeping: ' + max_age)
        time.sleep(int(max_age))
        status_response = fi_calculations_api.get_calculation_status_by_id(id=calculation_id)

    if status_response[1] != 201:
        print_error(status_response)
        sys.exit()

    output_calculation_result(status_response[0])


def output_calculation_result(result):
    print("Calculation Result")
    stachBuilder = StachExtensionFactory.get_row_organized_builder(StachVersion.V2)
    stachExtension = stachBuilder.set_package(result).build()
    dataFramesList = stachExtension.convert_to_dataframe()
    print(dataFramesList)
    # generate_excel(dataFramesList)  # Uncomment this line to get the result in table format exported to excel file.


def generate_excel(data_frames_list):
    for dataFrame in data_frames_list:
        writer = pd.ExcelWriter(str(uuid.uuid1()) + ".xlsx") # pylint: disable=abstract-class-instantiated
        dataFrame.to_excel(excel_writer=writer)
        writer.save()
        writer.close()


def print_error(response):
    print("Calculation Failed!!!")
    print("Status Code: " + str(response[1]))
    print("Request Key: " + response[2].get("x-datadirect-request-key"))
    print(response[0])


if __name__ == '__main__':
    main()
