import time
import os
import uuid
import pandas as pd
import urllib3

from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api.pa_calculations_api import PACalculationsApi
from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.api.pricing_sources_api import PricingSourcesApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.component_summary import ComponentSummary
from fds.analyticsapi.engines.model.pa_calculation_parameters_root import PACalculationParametersRoot
from fds.analyticsapi.engines.model.pa_calculation_parameters import PACalculationParameters
from fds.analyticsapi.engines.model.pa_date_parameters import PADateParameters
from fds.analyticsapi.engines.model.pa_identifier import PAIdentifier
from fds.analyticsapi.engines.model.pa_calculation_data_sources import PACalculationDataSources
from fds.analyticsapi.engines.model.pa_calculation_pricing_source import PACalculationPricingSource
from fds.protobuf.stach.extensions.StachVersion import StachVersion
from fds.protobuf.stach.extensions.StachExtensionFactory import StachExtensionFactory
from fds.protobuf.stach.extensions.v2.StachUtilities import StachUtilities

from urllib3 import Retry
urllib3.disable_warnings()

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

    components_api = ComponentsApi(api_client)
    pricingsources_api = PricingSourcesApi(api_client)

    try:
        pa_document_name = "pa3_documents:/pa_api_default_document-rbics"
        pa_component_name = "Multiple Portfolios"
        pa_component_category = "Exposures & Characteristics / Exposures & Characteristics"
        portfolio = "LION:100D-GB"
        benchmark = "LION:OEF-US"
        startdate = ""
        enddate = "20240508"
        frequency = "Single"
        currency = "USD"
        holdings = "B&H"
        pricing_source_name = "MSCI - Gross"
        pricing_source_category = "MSCI"
        pricing_source_directory = "Equity"

        # uncomment the below code line to setup cache control; max-stale=0 will be a fresh adhoc run and the max-stale value is in seconds.
        # Results are by default cached for 12 hours; Setting max-stale=300 will fetch a cached result which is 5 minutes older.
        # cache_control = "max-stale=0"
        get_components_response = components_api.get_pa_components(document=pa_document_name)
        component_id = [id for id in list(
            get_components_response[0].data.keys()) if get_components_response[0].data[id].name == pa_component_name and
                        get_components_response[0].data[id].category == pa_component_category][0]
        print("PA Component Id: " + component_id)
        pa_accounts = [PAIdentifier(id=portfolio, holdingsmode=holdings)]
        pa_benchmarks = [PAIdentifier(id=benchmark, holdingsmode=holdings)]

        pa_dates = PADateParameters(
            startdate=startdate, enddate=enddate, frequency=frequency)

        get_pricing_sources_response = pricingsources_api.get_pa_pricing_sources(name=pricing_source_name,
                                                                                 category=pricing_source_category,
                                                                                 directory=pricing_source_directory)
        pricing_source_id = [id for id in list(
            get_pricing_sources_response[0].data.keys()) if
                             get_pricing_sources_response[0].data[id].name == pricing_source_name
                             and get_pricing_sources_response[0].data[id].category == pricing_source_category
                             and get_pricing_sources_response[0].data[id].directory == pricing_source_directory][0]

        print("PA Pricing Source Id: " + pricing_source_id)

        pa_pricing_sources = [PACalculationPricingSource(id=pricing_source_id)]

        pa_datasources = PACalculationDataSources(portfoliopricingsources=pa_pricing_sources,
                                                  useportfoliopricingsourcesforbenchmark=True)

        pa_calculation_parameters = {"1": PACalculationParameters(componentid=component_id, accounts=pa_accounts,
                                                                  benchmarks=pa_benchmarks, dates=pa_dates,
                                                                  currencyisocode=currency, datasources=pa_datasources)}
        pa_calculation_parameter_root = PACalculationParametersRoot(
            data=pa_calculation_parameters)
        pa_calculations_api = PACalculationsApi(api_client)

        post_and_calculate_response = pa_calculations_api.post_and_calculate(
            pa_calculation_parameters_root=pa_calculation_parameter_root)
        # comment the above line and uncomment the below line to run the request with the cache_control header defined earlier
        # post_and_calculate_response = pa_calculations_api.post_and_calculate(pa_calculation_parameters_root=pa_calculation_parameter_root, cache_control=cache_control)
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

            status_response = pa_calculations_api.get_calculation_status_by_id(id=calculation_id)

            while status_response[1] == 202 and (status_response[0].data.status in ("Queued", "Executing")):
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = pa_calculations_api.get_calculation_status_by_id(calculation_id)

            for (calculation_unit_id, calculation_unit) in status_response[0].data.units.items():
                if calculation_unit.status == "Success":
                    print("Calculation Unit Id: " +
                          calculation_unit_id + " Succeeded!!!")
                    result_response = pa_calculations_api.get_calculation_unit_result_by_id(id=calculation_id,
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
    metadata_list = []
    stachBuilder = StachExtensionFactory.get_row_organized_builder(StachVersion.V2)
    stachExtension = stachBuilder.set_package(result).build()
    dataFramesList = stachExtension.convert_to_dataframe()
    MetaData = stachExtension.get_metadata()
    print(dataFramesList)
    print('\n MetaData:')
    for metadataItem in MetaData:
        metadata_dict = {}
        for keyName in metadataItem:
            appendedMetadata = ','.join(str(StachUtilities.get_value(x)) for x in metadataItem[keyName])
            metadata_dict[keyName] = appendedMetadata
        metadata_list.append(metadata_dict)

    metadata_df = pd.DataFrame(metadata_list)
    # Set display options for better readability
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    # Print the organized DataFrame

    print(metadata_df.to_string(index=False, header=True, justify='left', col_space=20))
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