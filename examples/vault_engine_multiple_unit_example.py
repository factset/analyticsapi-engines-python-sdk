import time
import os
import uuid
import pandas as pd

from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api.vault_calculations_api import VaultCalculationsApi
from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.api.configurations_api import ConfigurationsApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.component_summary import ComponentSummary
from fds.analyticsapi.engines.model.vault_calculation_parameters_root import VaultCalculationParametersRoot
from fds.analyticsapi.engines.model.vault_calculation_parameters import VaultCalculationParameters
from fds.analyticsapi.engines.model.vault_date_parameters import VaultDateParameters
from fds.analyticsapi.engines.model.vault_identifier import VaultIdentifier
from fds.protobuf.stach.extensions.StachVersion import StachVersion
from fds.protobuf.stach.extensions.StachExtensionFactory import StachExtensionFactory

from urllib3 import Retry

host = "https://api.factset.com"
username = os.environ["ANALYTICS_API_QAR_USERNAME_SERIAL"]
password = os.environ["ANALYTICS_API_QAR_PASSWORD"]


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
        vault_document_name = "Client:/aapi/VAULT_QA_PI_DEFAULT_LOCKED"
        vault_component_total_returns = "Total Returns"
        vault_component_performance = "Performance Over Time"
        vault_component_category = "Performance / Performance Relative Dates"
        vault_default_account = "CLIENT:/BISAM/REPOSITORY/QA/SMALL_PORT.ACCT"
        vault_startdate = "20180101"
        vault_enddate = "20180329"
        frequency = "Monthly"

        get_components_response = components_api.get_vault_components(vault_document_name)
        component_total_returns_summary = ComponentSummary(
            name=vault_component_total_returns, category=vault_component_category)
        component_total_returns_id = [id for id in list(get_components_response[0].data.keys(
        )) if get_components_response[0].data[id] == component_total_returns_summary][0]
        print("Vault Total Returns Component Id: " + component_total_returns_id)

        component_performance_summary = ComponentSummary(
            name=vault_component_performance, category=vault_component_category)
        component_performance_id = [id for id in list(get_components_response[0].data.keys(
        )) if get_components_response[0].data[id] == component_performance_summary][0]
        print("Vault Performance Over Time Component Id: " +
              component_performance_id)

        vault_account_identifier = VaultIdentifier(vault_default_account)
        vault_dates = VaultDateParameters(
            startdate=vault_startdate, enddate=vault_enddate, frequency=frequency)

        configurations_api = ConfigurationsApi(api_client)
        get_vault_configurations_response = configurations_api.get_vault_configurations(
            vault_default_account)
        configuration_id = list(get_vault_configurations_response[0].data.keys())[0]

        vault_calculation_parameters = {
            "total_returns": VaultCalculationParameters(componentid=component_total_returns_id, account=vault_account_identifier, dates=vault_dates, configid=configuration_id),
            "performance_over_time": VaultCalculationParameters(componentid=component_performance_id, account=vault_account_identifier, dates=vault_dates, configid=configuration_id)}

        vault_calculation_parameters_root = VaultCalculationParametersRoot(
            data=vault_calculation_parameters)

        vault_calculations_api = VaultCalculationsApi(api_client)

        post_and_calculate_response = vault_calculations_api.post_and_calculate(
            vault_calculation_parameters_root=vault_calculation_parameters_root)

        if post_and_calculate_response[1] == 202 or post_and_calculate_response[1] == 200:
            calculation_id = post_and_calculate_response[0].data.calculationid
            print("Calculation Id: " + calculation_id)

            status_response = vault_calculations_api.get_calculation_status_by_id(id=calculation_id)

            while status_response[1] == 202 and (status_response[0].data.status in ("Queued", "Executing")):
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = vault_calculations_api.get_calculation_status_by_id(calculation_id)

            for (calculation_unit_id, calculation_unit) in status_response[0].data.units.items():
                if calculation_unit.status == "Success":
                    print("Calculation Unit Id: " +
                          calculation_unit_id + " Succeeded!!!")
                    result_response = vault_calculations_api.get_calculation_unit_result_by_id(id=calculation_id,
                                                                                               unit_id=calculation_unit_id)
                    output_calculation_result(result_response[0]['data'])
                else:
                    print("Calculation Unit Id:" +
                          calculation_unit_id + " Failed!!!")
                    print("Error message : " + str(calculation_unit.errors))
        else:
            print("Calculation creation failed")
            print("Error status : " + str(post_and_calculate_response[1]))
            print("Error message : " + str(post_and_calculate_response[0]))

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
