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
from fds.analyticsapi.engines.api.columns_api import ColumnsApi
from fds.analyticsapi.engines.api.column_statistics_api import ColumnStatisticsApi
from fds.analyticsapi.engines.model.column_statistic import ColumnStatistic
from fds.analyticsapi.engines.api.groups_api import GroupsApi
from fds.analyticsapi.engines.model.group import Group

from urllib3 import Retry

host = os.environ['FACTSET_HOST']
fds_username = os.environ['FACTSET_USERNAME']
fds_api_key = os.environ['FACTSET_API_KEY']
#proxy_url = os.environ['PROXY_URL']

def main():
    config = Configuration()
    config.host = host
    config.username = fds_username
    config.password = fds_api_key
    config.discard_unknown_keys = True
    # add proxy and/or disable ssl verification according to your development environment
    # config.proxy = proxy_url
    config.verify_ssl = False

    # Setting configuration to retry api calls on http status codes of 429 and 503.
    config.retries = Retry(total=3, status=3, status_forcelist=frozenset([429, 503]), backoff_factor=2,
                           raise_on_status=False)

    api_client = ApiClient(configuration=config)

    try:
        column_name = "Port. Average Weight"
        column_category = "Portfolio/Position Data"
        column_statistic_name = "Active Weights"

        group_category = "Country & Region/JP Morgan/JP Morgan CEMBI "
        group_name = "Country - JP Morgan CEMBI "

        unlinked_pa_template_directory = "Personal:UnlinkedPATemplates/"
        unlinked_pa_template_type_id = "996E90B981AEE83F14029ED3D309FB3F03EC6E2ACC7FD42C22CBD5D279502CFD"

        templated_pa_component_directory = "Personal:TemplatedPAComponents/"

        portfolio = "BENCH:SP50"
        benchmark = "BENCH:R.1000"
        startdate = "20180101"
        enddate = "20181231"
        frequency = "Monthly"
        currencyisocode = "USD"
        componentdetail = "GROUPS"
        directory = "Factset"

        # uncomment the below code line to setup cache control; max-stale=0 will be a fresh adhoc run and the max-stale value is in seconds.
        # Results are by default cached for 12 hours; Setting max-stale=300 will fetch a cached result which is 5 minutes older. 
        # cache_control = "max-stale=0"

        # get column id
        columns_api = ColumnsApi(api_client=api_client)
        column = columns_api.get_pa_columns(
            name = column_name,
            category = column_category,
            directory = directory
        )
        column_id = list(column[0].data.keys())[0]

        # get column statistics id
        column_statistics_api = ColumnStatisticsApi(api_client=api_client)
        get_all_column_statistics = column_statistics_api.get_pa_column_statistics()
        column_statistic_id = [id for id in list(
            get_all_column_statistics[0].data.keys()) if get_all_column_statistics[0].data[id].name == column_statistic_name][0]

        # create columns parameter
        columns = [PACalculationColumn(id=column_id, statistics=[column_statistic_id])]

        # get group id
        groups_api = GroupsApi(api_client=api_client)
        groups = groups_api.get_pa_groups()
        group_id = [id for id in list(
            groups[0].data.keys()) if groups[0].data[id].category == group_category and 
                                      groups[0].data[id].directory == directory and
                                      groups[0].data[id].name == group_name][0]

        # create groups parameter
        groups = [PACalculationGroup(id=group_id)]

        # create an unlinked PA template
        unlinked_pa_template_parameters = UnlinkedPATemplateParameters(
            directory=unlinked_pa_template_directory,
            template_type_id=unlinked_pa_template_type_id,
            description="This is an unlinked PA template that only returns security level data",
            accounts = [PAIdentifier(id=portfolio)],
            benchmarks = [PAIdentifier(id=benchmark)],
            columns = columns,
            dates = PADateParameters(
                startdate = startdate,
                enddate = enddate,
                frequency = frequency),
            groups = groups,
            currencyisocode = currencyisocode,
            componentdetail = componentdetail,
            content = TemplateContentTypes(
                mandatory = ["accounts", "benchmarks"],
                optional = ["groups", "columns", "currencyisocode", "componentdetail"],
                locked = ["dates"])
        )

        unlinked_pa_template_parameters_root = UnlinkedPATemplateParametersRoot(
            data = unlinked_pa_template_parameters
        )

        unlinked_pa_template_api = UnlinkedPATemplatesApi(api_client=api_client)

        response = unlinked_pa_template_api.create_unlinked_pa_templates(
            unlinked_pa_template_parameters_root = unlinked_pa_template_parameters_root)

        # create a templated PA component
        parent_template_id = response[0].data.get("id")

        templated_pa_component_parameters = TemplatedPAComponentParameters(
            directory=templated_pa_component_directory,
            parent_template_id=parent_template_id,
            description="This is a templated PA component",
            component_data = PAComponentData(
                accounts = [PAIdentifier(id=portfolio)],
                benchmarks = [PAIdentifier(id=benchmark)],
                columns = columns,
                groups = groups,
                currencyisocode = currencyisocode,
                componentdetail = componentdetail
            )
        )

        templated_pa_component_parameters_root = TemplatedPAComponentParametersRoot(
            data = templated_pa_component_parameters
        )

        templated_pa_components_api = TemplatedPAComponentsApi(api_client)

        response = templated_pa_components_api.create_templated_pa_components(
            templated_pa_component_parameters_root = templated_pa_component_parameters_root)

        component_id = response[0].data.get("id")

        print("PA Component Id: " + component_id)

        # do PA calculation with given templated component id
        pa_accounts = [PAIdentifier(id=portfolio)]
        pa_benchmarks = [PAIdentifier(id=benchmark)]
        pa_dates = PADateParameters(
            startdate=startdate, enddate=enddate, frequency=frequency)

        pa_calculation_parameters = {"1": PACalculationParameters(componentid=component_id, accounts=pa_accounts,
                                                                  benchmarks=pa_benchmarks, dates=pa_dates),
                                     "2": PACalculationParameters(componentid=component_id, accounts=pa_accounts,
                                                                  benchmarks=pa_benchmarks, dates=pa_dates)}

        pa_calculation_parameter_root = PACalculationParametersRoot(
            data=pa_calculation_parameters)

        pa_calculations_api = PACalculationsApi(api_client=api_client)

        post_and_calculate_response = pa_calculations_api.post_and_calculate(
            pa_calculation_parameters_root=pa_calculation_parameter_root)

        # comment the above line and uncomment the below line to run the request with the cache_control header defined earlier
        # post_and_calculate_response = pa_calculations_api.post_and_calculate(pa_calculation_parameters_root=pa_calculation_parameter_root, cache_control=cache_control)
        if post_and_calculate_response[1] == 202 or post_and_calculate_response[1] == 200:
            calculation_id = post_and_calculate_response[0].data.calculationid
            print("Calculation Id: " + calculation_id)

            status_response = pa_calculations_api.get_calculation_status_by_id(id=calculation_id)

            while status_response[1] == 202:
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
                    output_calculation_result(result=result_response[0]['data'])
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
    stachExtension = stachBuilder.set_package(pkg=result).build()
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
