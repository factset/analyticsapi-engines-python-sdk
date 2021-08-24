import time
import os
import uuid
import pandas as pd

from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api.pa_calculations_api import PACalculationsApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.pa_calculation_parameters_root import PACalculationParametersRoot
from fds.analyticsapi.engines.model.pa_calculation_parameters import PACalculationParameters
from fds.analyticsapi.engines.model.pa_date_parameters import PADateParameters
from fds.analyticsapi.engines.model.pa_identifier import PAIdentifier
from fds.protobuf.stach.extensions.StachVersion import StachVersion
from fds.protobuf.stach.extensions.StachExtensionFactory import StachExtensionFactory
from fds.analyticsapi.engines.api.templated_pa_components_api import TemplatedPAComponentsApi
from fds.analyticsapi.engines.api.unlinked_pa_templates_api import UnlinkedPATemplatesApi
from fds.analyticsapi.engines.model.templated_pa_component_parameters import TemplatedPAComponentParameters
from fds.analyticsapi.engines.model.templated_pa_component_parameters_root import TemplatedPAComponentParametersRoot
from fds.analyticsapi.engines.model.pa_component_data import PAComponentData
from fds.analyticsapi.engines.model.pa_date_parameters import PADateParameters
from fds.analyticsapi.engines.model.pa_identifier import PAIdentifier
from fds.analyticsapi.engines.model.pa_calculation_group import PACalculationGroup
from fds.analyticsapi.engines.model.pa_calculation_column import PACalculationColumn
from fds.analyticsapi.engines.model.unlinked_pa_template_parameters import UnlinkedPATemplateParameters
from fds.analyticsapi.engines.model.template_content_types import TemplateContentTypes
from fds.analyticsapi.engines.model.unlinked_pa_template_parameters_root import UnlinkedPATemplateParametersRoot

from urllib3 import Retry

host = "https://api.staging-cauth.factset.com"
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

    templated_pa_components_api = TemplatedPAComponentsApi(api_client)
    unlinked_pa_template_api = UnlinkedPATemplatesApi(api_client)

    try:
        pa_benchmark_sp_50 = "BENCH:SP50"
        pa_benchmark_r_1000 = "BENCH:R.1000"
        startdate = "20180101"
        enddate = "20181231"
        frequency = "Monthly"

        # create an unlinked PA template
        unlinked_pa_template_parameters = UnlinkedPATemplateParameters(
            directory="Personal:UnlinkedPATemplates/",
            template_type_id="996E90B981AEE83F14029ED3D309FB3F03EC6E2ACC7FD42C22CBD5D279502CFD",
            description="This is an unlinked PA template that only returns security level data",
            accounts = [
                PAIdentifier(
                    id = "SPN:SP50",
                    holdingsmode = "B&H"),
                PAIdentifier(
                    id = "MSCI_USA:984000",
                    holdingsmode = "B&H")],
            benchmarks = [
                PAIdentifier(
                    id = "SPN:SP50",
                    holdingsmode = "B&H"),
                PAIdentifier(
                    id = "DJGX:AMERICAS",
                    holdingsmode = "B&H")],
            columns = [
                PACalculationColumn(
                    id = "BD1720474AB8A80BDD79777F5B9CA594F4151C0554E30F9C916BA73BFAFC1FE0",
                    statistics = ["eb9d6d91416e4224bacadc261787e56f"])],
            dates = PADateParameters(
                startdate = "20200101",
                enddate = "20201215",
                frequency = "Monthly"),
            groups = [
                PACalculationGroup(id = "5BCFFD17598FAEBD88EB4934EFB5FEF53849867D607ECEF232CD42D3369BBBCA")],
            currencyisocode = "USD",
            componentdetail = "GROUPS",
            content = TemplateContentTypes(
                mandatory = ["accounts", "benchmarks"],
                optional = ["groups", "columns", "currencyisocode", "componentdetail"],
                locked = ["dates"])
        )

        unlinked_pa_template_parameters_root = UnlinkedPATemplateParametersRoot(
            data = unlinked_pa_template_parameters
        )

        response = unlinked_pa_template_api.create_unlinked_pa_templates(
            unlinked_pa_template_parameters_root = unlinked_pa_template_parameters_root)

        parent_template_id = list(response[0].data.keys())[0]

        # create a templated component
        templated_pa_component_parameters = TemplatedPAComponentParameters(
            directory="Personal:TemplatedPAComponents/",
            parent_template_id=parent_template_id,
            description="This is a templated PA component",
            component_data = PAComponentData(
                accounts = [
                    PAIdentifier(
                        id = "SPN:SP50",
                        holdingsmode = "B&H"),
                    PAIdentifier(
                        id = "MSCI_USA:984000",
                        holdingsmode = "B&H")],
                benchmarks = [
                    PAIdentifier(
                        id = "SPN:SP50",
                        holdingsmode = "B&H"),
                    PAIdentifier(
                        id = "DJGX:AMERICAS",
                        holdingsmode = "B&H")],
                columns = [
                    PACalculationColumn(
                        id = "BD1720474AB8A80BDD79777F5B9CA594F4151C0554E30F9C916BA73BFAFC1FE0",
                        statistics = ["eb9d6d91416e4224bacadc261787e56f"])],
                groups = [
                    PACalculationGroup(id = "5BCFFD17598FAEBD88EB4934EFB5FEF53849867D607ECEF232CD42D3369BBBCA")],
                currencyisocode = "USD",
                componentdetail = "GROUPS"
            )
        )

        templated_pa_component_parameters_root = TemplatedPAComponentParametersRoot(
            data = templated_pa_component_parameters
        )
        response = templated_pa_components_api.create_templated_pa_components(
            templated_pa_component_parameters_root = templated_pa_component_parameters_root)

        component_id = list(response[0].data.keys())[0]

        print("PA Component Id: " + component_id)

        # do PA calculation with given templated component id
        pa_accounts = [PAIdentifier(id=pa_benchmark_sp_50)]
        pa_benchmarks = [PAIdentifier(id=pa_benchmark_r_1000)]
        pa_dates = PADateParameters(
            startdate=startdate, enddate=enddate, frequency=frequency)

        pa_calculation_parameters = {"1": PACalculationParameters(componentid=component_id, accounts=pa_accounts,
                                                                  benchmarks=pa_benchmarks, dates=pa_dates)}

        pa_calculation_parameter_root = PACalculationParametersRoot(
            data=pa_calculation_parameters)

        pa_calculations_api = PACalculationsApi(api_client)

        post_and_calculate_response = pa_calculations_api.post_and_calculate(
            pa_calculation_parameters_root=pa_calculation_parameter_root)

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
