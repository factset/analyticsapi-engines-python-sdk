import sys
import time
import uuid
import os
import pandas as pd

from fds.analyticsapi.engines.api.fi_calculations_api import FICalculationsApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.fi_calculation_parameters import FICalculationParameters
from fds.analyticsapi.engines.model.fi_calculation_parameters_root import FICalculationParametersRoot
from fds.analyticsapi.engines.model.fi_security import FISecurity
from fds.analyticsapi.engines.model.fi_job_settings import FIJobSettings
from fds.protobuf.stach.extensions.StachVersion import StachVersion
from fds.protobuf.stach.extensions.StachExtensionFactory import StachExtensionFactory
from fds.analyticsapi.engines.model.fi_market_environment import FIMarketEnvironment

from urllib3 import Retry

host = os.environ['FACTSET_HOST']
fds_username = os.environ['FACTSET_USERNAME']
fds_api_key = os.environ['FACTSET_API_KEY']

def main():
    config = Configuration()
    config.host = host
    config.username = fds_username
    config.password = fds_api_key
    config.discard_unknown_keys = True
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
                    "Effective Convexity",
                    "CF Coupon"]

    security1 = FISecurity(
        calc_from_method = "Price",
        calc_from_value = 100.285,
        face = 10000.0,
        symbol = "912828ZG8",
        settlement = "20201202",
        discount_curve = "UST"
    )
    security2 = FISecurity(
        calc_from_method = "Price",
        calc_from_value = 101.138,
        face = 200000.0,
        symbol = "US037833AR12",
        settlement = "20201203",
        discount_curve = "UST"
    )
    rate_path = FIMarketEnvironment(
        rate_path = "FLAT & FORWARD"
    )
    

    # uncomment the below code line to setup cache control; max-stale=0 will be a fresh adhoc run and the max-stale value is in seconds.
    # Results are by default cached for 12 hours; Setting max-stale=300 will fetch a cached result which is 5 minutes older. 
    # cache_control = "max-stale=0"

    securities = [security1, security2]

    jobSettings = FIJobSettings(as_of_date="20201201",partial_duration_months =[1,3,6], market_environment=rate_path)

    fi_calculation_parameters = FICalculationParameters(securities, calculations, jobSettings)

    fi_calculation_parameters_root = FICalculationParametersRoot(data=fi_calculation_parameters)

    fi_calculations_api = FICalculationsApi(api_client)
    run_calculation_response = fi_calculations_api.post_and_calculate(
        fi_calculation_parameters_root=fi_calculation_parameters_root)
    # comment the above line and uncomment the below line to run the request with the cache_control header defined earlier
    # run_calculation_response = fi_calculations_api.post_and_calculate(
        # fi_calculation_parameters_root=fi_calculation_parameters_root, cache_control=cache_control)
    if run_calculation_response[1] != 202 and run_calculation_response[1] != 201:
        print_error(run_calculation_response)
        sys.exit()

    if run_calculation_response[1] == 201:
        output_calculation_result(run_calculation_response[0].data)
        sys.exit()

    calculation_id = run_calculation_response[2]["X-Factset-Api-Calculation-Id"]
    print("Calculation Id: " + calculation_id)

    status_response = fi_calculations_api.get_calculation_status_by_id(
        id=calculation_id)
    while status_response[1] == 202:
        max_age = '5'
        age_value = status_response[2].get("cache-control")
        if age_value is not None:
            max_age = age_value.replace("max-age=", "")
        print('Sleeping: ' + max_age)
        time.sleep(int(max_age))
        status_response = fi_calculations_api.get_calculation_status_by_id(
            id=calculation_id)

    if status_response[1] != 201:
        print_error(status_response)
        sys.exit()

    output_calculation_result(status_response[0].data)


def output_calculation_result(result):
    print("Calculation Result")
    stachBuilder = StachExtensionFactory.get_row_organized_builder(
        StachVersion.V2)
    stachExtension = stachBuilder.set_package(result).build()
    dataFramesList = stachExtension.convert_to_dataframe()
    print(dataFramesList)
    # generate_excel(dataFramesList)  # Uncomment this line to get the result in table format exported to excel file.


def generate_excel(data_frames_list):
    for dataFrame in data_frames_list:
        writer = pd.ExcelWriter(  # pylint: disable=abstract-class-instantiated
            str(uuid.uuid1()) + ".xlsx")
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
