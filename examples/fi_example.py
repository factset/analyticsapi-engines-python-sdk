import json
import sys
import time
import pandas as pd
import uuid
import os

from fds.analyticsapi.engines import ComponentSummary
from fds.analyticsapi.engines.api.fi_calculations_api import FICalculationsApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.models.fi_calculation_parameters import FICalculationParameters
from fds.analyticsapi.engines.models.security import Security
from fds.analyticsapi.engines.models.job_settings import JobSettings
from fds.analyticsapi.engines.stach_extensions import StachExtensions
from fds.protobuf.stach.Package_pb2 import Package

from google.protobuf import json_format
from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import MessageToDict
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
   
    security1 = Security("Price", 100.285, 10000.0, "912828ZG8", "20201202", "UST")
    security2 = Security("Price", 101.138, 200000.0, "US037833AR12", "20201203", "UST")
    
    securities = [security1, security2]

    jobSettings = JobSettings("20201201")
    
    fi_calculation_parameters = FICalculationParameters(securities, calculations, jobSettings)

    print(fi_calculation_parameters)

    fi_calculations_api = FICalculationsApi(api_client)
    run_calculation_response = fi_calculations_api.run_fi_calculation_with_http_info(fi_calculation_parameters = fi_calculation_parameters)

    if run_calculation_response[1] != 202 and run_calculation_response[1] != 201:
        print_error(run_calculation_response)
        sys.exit()

    if run_calculation_response[1] == 201:
        print_result(run_calculation_response[0])
        sys.exit()

    calculation_id = run_calculation_response[2].get("location").split("/")[-1]
    print("Calculation Id: " + calculation_id)

    status_response = fi_calculations_api.get_fi_calculation_by_id_with_http_info(calculation_id)
    while status_response[1] == 202:
        max_age = '5'
        age_value = status_response[2].get("cache-control")
        if age_value is not None:
            max_age = age_value.replace("max-age=", "")
        print('Sleeping: ' + max_age)
        time.sleep(int(max_age))
        status_response = fi_calculations_api.get_fi_calculation_by_id_with_http_info(calculation_id)

    if status_response[1] != 200:
        print_error(status_response)
        sys.exit()

    print_result(status_response[0])


def print_result(response):
    # converting the data to Package object
    result = json_format.Parse(json.dumps(response), Package())
    # print(MessageToJson(result)) # To print the result object as a JSON
    # print(MessageToDict(result)) # To print the result object as a Dictionary
    tables = StachExtensions.convert_to_table_format(result)  # To convert result to 2D tables.
    print(tables[0])  # Prints the result in 2D table format.
    # generate_excel(result)  # Uncomment this line to get the result in table format exported to excel file.


def generate_excel(package):
    for table in StachExtensions.convert_to_table_format(package):
        writer = pd.ExcelWriter(str(uuid.uuid1()) + ".xlsx")
        table.to_excel(excel_writer=writer)
        writer.save()
        writer.close()


def print_error(response):
    print("Calculation Failed!!!")
    print("Status Code: " + str(response[1]))
    print("Request Key: " + response[2].get("x-datadirect-request-key"))
    print(response[0])


if __name__ == '__main__':
    main()
