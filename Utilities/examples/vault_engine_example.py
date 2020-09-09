import json
import sys
import time
import pandas as pd
import uuid

from fds.analyticsapi.engines import ComponentSummary, ApiException
from fds.analyticsapi.engines.api.calculations_api import CalculationsApi
from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.api.configurations_api import ConfigurationsApi
from fds.analyticsapi.engines.api.utility_api import UtilityApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.models.calculation import Calculation
from fds.analyticsapi.engines.models.vault_calculation_parameters import VaultCalculationParameters
from fds.analyticsapi.engines.models.vault_date_parameters import VaultDateParameters
from fds.analyticsapi.engines.models.vault_identifier import VaultIdentifier
from fds.analyticsapi.engines.stach_extensions import StachExtensions
from fds.protobuf.stach.Package_pb2 import Package

from google.protobuf import json_format
from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import MessageToDict
from urllib3 import Retry

host = "https://api.factset.com"
username = "<username-serial>"
password = "<apiKey>"

vault_document_name = "PA3_DOCUMENTS:DEFAULT"
vault_component_name = "Weights"
vault_component_category = "General / Positioning"
vault_default_account = "Client:/analytics/data/US_MID_CAP_CORE.ACTM"
vault_startdate = "FIRST_REPOSITORY"
vault_enddate = "LAST_REPOSITORY"
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
    config.retries = Retry(total=3, status=3, status_forcelist=frozenset([429, 503]), backoff_factor=2,
                           raise_on_status=False)

    api_client = ApiClient(config)

    components_api = ComponentsApi(api_client)

    try:
        components = components_api.get_vault_components(vault_document_name)
        component_desc = ComponentSummary(name=vault_component_name, category=vault_component_category)
        component_id = [id for id in list(components.keys()) if components[id] == component_desc][0]
        print("Vault Component Id: " + component_id)
        vault_account_identifier = VaultIdentifier(vault_default_account)
        vault_dates = VaultDateParameters(vault_startdate, vault_enddate, frequency)

        configurations_api = ConfigurationsApi(api_client)
        configurations = configurations_api.get_vault_configurations(vault_default_account)
        configuration_id = list(configurations.keys())[0]

        vault_calculation_parameters = {
            "3": VaultCalculationParameters(component_id, vault_account_identifier, vault_dates, configuration_id)}

        calculation = Calculation(vault=vault_calculation_parameters)

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

        for (calculation_unit, calculation_unit_id) in zip(status_response[0].vault.values(), status_response[0].vault):
            if calculation_unit.status == "Success":
                print("Calculation Unit Id: " + calculation_unit_id + " Succeeded!!!")
                utility_api = UtilityApi(api_client)
                result_response = utility_api.get_by_url_with_http_info(calculation_unit.result)

                print("Calculation Result")
                # converting the data to Package object
                result = json_format.Parse(json.dumps(result_response[0]), Package())
                # print(MessageToJson(result)) # To print the result object as a JSON
                # print(MessageToDict(result)) # To print the result object as a Dictionary
                tables = StachExtensions.convert_to_table_format(result)  # To convert result to 2D tables.
                print(tables[0])  # Prints the result in 2D table format.
                # generate_excel(result)  # Uncomment this line to get the result in table format exported to excel file.
            else:
                print("Calculation Unit Id:" + calculation_unit_id + " Failed!!!")
                print("Error message : " + calculation_unit.error)

    except ApiException as e:
        print("Api exception Encountered")
        print(e)
        exit()


def generate_excel(package):
    for table in StachExtensions.convert_to_table_format(package):
        writer = pd.ExcelWriter(str(uuid.uuid1()) + ".xlsx")
        table.to_excel(excel_writer=writer)
        writer.save()
        writer.close()


if __name__ == '__main__':
    main()
