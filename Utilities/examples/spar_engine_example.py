import json
import sys
import time

from fds.analyticsapi.engines import ComponentSummary, ApiException
from fds.analyticsapi.engines.api.calculations_api import CalculationsApi
from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.api.utility_api import UtilityApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.models.calculation import Calculation
from fds.analyticsapi.engines.models.spar_calculation_parameters import SPARCalculationParameters
from fds.analyticsapi.engines.models.spar_date_parameters import SPARDateParameters
from fds.analyticsapi.engines.models.spar_identifier import SPARIdentifier
from fds.protobuf.stach.Package_pb2 import Package

from google.protobuf import json_format
from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import MessageToDict
from urllib3 import Retry

# Copy 'Converting API output to Table Format' snippet to a file with name 'stach_extensions.py' to use below import statement
from stach_extensions import StachExtensions

host = "https://api.factset.com"
username = "<username-serial>"
password = "<apiKey>"

spar_document_name = "pmw_root:/spar_documents/Factset Default Document"
spar_component_name = "Returns Table"
spar_component_category = "Raw Data / Returns"
spar_benchmark_r_1000 = "R.1000"
spar_benchmark_russell_pr_2000 = "RUSSELL_P:R.2000"
spar_benchmark_russell_prefix = "RUSSELL"
spar_benchmark_russell_return_type = "GTR"
startdate = "20180101"
enddate = "20181231"
frequency = "Monthly"


def main():
    config = Configuration()
    config.host = host
    config.username = username
    config.password = password
    # add proxy and/or disable ssl verification according to your development environment
    # config.proxy = "<proxyUrl>"
    config.verify_ssl = False

    # Setting configuration to retry api calls on http status codes of 429 and 503.
    config.retries = Retry(total=3, status=3, status_forcelist=frozenset([429, 503]), backoff_factor=2, raise_on_status=False)

    api_client = ApiClient(config)

    components_api = ComponentsApi(api_client)

    try:
        components = components_api.get_spar_components(spar_document_name)
        component_desc = ComponentSummary(name=spar_component_name, category=spar_component_category)
        component_id = [id for id in list(components.keys()) if components[id] == component_desc][0]
        print("SPAR Component Id: " + component_id)
        spar_account_identifier = SPARIdentifier(spar_benchmark_r_1000, spar_benchmark_russell_return_type, spar_benchmark_russell_prefix)
        spar_accounts = [spar_account_identifier]
        spar_benchmark_identifier = SPARIdentifier(spar_benchmark_russell_pr_2000, spar_benchmark_russell_return_type, spar_benchmark_russell_prefix)
        spar_dates = SPARDateParameters(startdate, enddate, frequency)

        spar_calculation_parameters = {"2": SPARCalculationParameters(component_id, spar_accounts, spar_benchmark_identifier, spar_dates)}

        calculation = Calculation(spar=spar_calculation_parameters)

        calculations_api = CalculationsApi(api_client)
        run_calculation_response = calculations_api.run_calculation_with_http_info(calculation=calculation)

        calculation_id = run_calculation_response[2].get("location").split("/")[-1]
        print("Calculation Id: " + calculation_id)

        status_response = calculations_api.get_calculation_status_by_id_with_http_info(calculation_id)
        while status_response[1] == 200 and (status_response[0].status in ("Queued", "Executing")):
            max_age = '5'
            age_value = status_response[2].get("cache-control")
            if age_value is not None:
                max_age = age_value.replace("max-age=", "")
            print('Sleeping: ' + max_age)
            time.sleep(int(max_age))
            status_response = calculations_api.get_calculation_status_by_id_with_http_info(calculation_id)

        for (calculation_unit, calculation_unit_id) in zip(status_response[0].spar.values(), status_response[0].spar):
            if calculation_unit.status == "Success":
                print("Calculation Unit Id: " + calculation_unit_id + " Succeeded!!!")
                utility_api = UtilityApi(api_client)
                result_response = utility_api.get_by_url_with_http_info(calculation_unit.result)

                print("Calculation Result")
                # converting the data to Package object
                result = json_format.Parse(json.dumps(result_response[0]), Package())
                # print(MessageToJson(result)) # To print the result object as a JSON
                # print(MessageToDict(result)) # To print the result object as a Dictionary
                tables = StachExtensions.convert_to_table_format(result) # To convert result to 2D tables.
                print(tables[0]) # Prints the result in 2D table format.
                # StachExtensions.generate_excel(result) # To get the result in table format exported to excel file.
            else:
                print("Calculation Unit Id:" + calculation_unit_id + " Failed!!!")
                print("Error message : " + calculation_unit.error)

    except ApiException as e:
        print("Api exception Encountered")
        print(e)
        exit()


if __name__ == '__main__':
    main()