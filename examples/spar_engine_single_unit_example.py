import time
import pandas as pd
import os
import uuid

from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api.spar_calculations_api import SPARCalculationsApi
from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.component_summary import ComponentSummary
from fds.analyticsapi.engines.model.spar_calculation_parameters_root import SPARCalculationParametersRoot
from fds.analyticsapi.engines.model.spar_calculation_parameters import SPARCalculationParameters
from fds.analyticsapi.engines.model.spar_date_parameters import SPARDateParameters
from fds.analyticsapi.engines.model.spar_identifier import SPARIdentifier
from fds.protobuf.stach.extensions.StachVersion import StachVersion
from fds.protobuf.stach.extensions.StachExtensionFactory import StachExtensionFactory

from urllib3 import Retry

host = "https://api.factset.com"
username = "<username-serial>"
password = "<apiKey>"


def main():
    config = Configuration()
    config.host = host
    config.username = username
    config.password = password
    config.discard_unknown_keys = True
    # add proxy and/or disable ssl verification according to your development environment
    # config.proxy = "<proxyUrl>"
    config.verify_ssl = False

    # Setting configuration to retry api calls on http status codes of 429 and 503.
    config.retries = Retry(total=3, status=3, status_forcelist=frozenset([429, 503]), backoff_factor=2,
                           raise_on_status=False)

    api_client = ApiClient(config)

    components_api = ComponentsApi(api_client)
    try:
        spar_document_name = "pmw_root:/spar_documents/Factset Default Document"
        spar_component_name = "Returns Table"
        spar_component_category = "Raw Data / Returns"
        spar_benchmark_1 = "R.1000"
        spar_benchmark_2 = "RUSSELL_P:R.2000"
        spar_benchmark_prefix = "RUSSELL"
        spar_benchmark_return_type = "GTR"
        startdate = "20180101"
        enddate = "20181231"
        frequency = "Monthly"
        # uncomment the below code line to setup cache control; max-stale=0 will be a fresh adhoc run and the max-stale value is in seconds.
        # Results are by default cached for 12 hours; Setting max-stale=300 will fetch a cached result which is 5 minutes older.
        # cache_control = "max-stale=0"
        get_components_response = components_api.get_spar_components(spar_document_name)
        
        component_id = [id for id in list(
            get_components_response[0].data.keys()) if get_components_response[0].data[id].name == spar_component_name and get_components_response[0].data[id].category == spar_component_category][0]
        print("SPAR Component Id: " + component_id)
        spar_account_identifier = SPARIdentifier(id=spar_benchmark_1, returntype=spar_benchmark_return_type,
                                                 prefix=spar_benchmark_prefix)
        spar_accounts = [spar_account_identifier]
        spar_benchmark_identifier = SPARIdentifier(id=spar_benchmark_2, returntype=spar_benchmark_return_type,
                                                   prefix=spar_benchmark_prefix)
        spar_dates = SPARDateParameters(startdate, enddate, frequency)

        spar_calculation_parameters = {"1": SPARCalculationParameters(componentid=component_id, accounts=spar_accounts, benchmark=spar_benchmark_identifier,
                                                                      dates=spar_dates)}

        spar_calculation_parameter_root = SPARCalculationParametersRoot(
            data=spar_calculation_parameters)

        spar_calculations_api = SPARCalculationsApi(api_client)
        post_and_calculate_response = spar_calculations_api.post_and_calculate(
            spar_calculation_parameters_root=spar_calculation_parameter_root)
        # comment the above line and uncomment the below line to run the request with the cache_control header defined earlier
        # post_and_calculate_response = spar_calculations_api.post_and_calculate(spar_calculation_parameters_root=spar_calculation_parameter_root, cache_control=cache_control)
        if post_and_calculate_response[1] == 201:
            output_calculation_result(post_and_calculate_response[0]['data'])
        elif post_and_calculate_response[1] == 200:
            for (calculation_unit_id, calculation_unit) in post_and_calculate_response[0].data.units.items():
                print("Calculation Unit Id:" +
                      calculation_unit_id + " Failed!!!")
                print("Error message : " + str(calculation_unit.errors))
        else:
            calculation_id = post_and_calculate_response[0].data.calculationid
            print("Calculation Id: " + calculation_id)

            status_response = spar_calculations_api.get_calculation_status_by_id(id=calculation_id)

            while status_response[1] == 202 and (status_response[0].data.status in ("Queued", "Executing")):
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = spar_calculations_api.get_calculation_status_by_id(calculation_id)

            for (calculation_unit_id, calculation_unit) in status_response[0].data.units.items():
                if calculation_unit.status == "Success":
                    print("Calculation Unit Id: " +
                          calculation_unit_id + " Succeeded!!!")
                    result_response = spar_calculations_api.get_calculation_unit_result_by_id(id=calculation_id,
                                                                                              unit_id=calculation_unit_id)
                    output_calculation_result(result_response[0]['data'])
                else:
                    print("Calculation Unit Id:" +
                          calculation_unit_id + " Failed!!!")
                    print("Error message : " + str(calculation_unit.errors))
    except ApiException as e:
        print("Api exception Encountered")
        print(e)
        exit()


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


if __name__ == '__main__':
    main()
