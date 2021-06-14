import time
import os
import uuid
import pandas as pd

from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api.quant_calculations_api import QuantCalculationsApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.quant_calculation_parameters_root import QuantCalculationParametersRoot
from fds.analyticsapi.engines.model.quant_calculation_parameters import QuantCalculationParameters
from fds.analyticsapi.engines.model.quant_screening_expression_universe import QuantScreeningExpressionUniverse
from fds.analyticsapi.engines.model.quant_fds_date import QuantFdsDate
from fds.analyticsapi.engines.model.quant_screening_expression import QuantScreeningExpression
from fds.analyticsapi.engines.model.quant_fql_expression import QuantFqlExpression
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

    try:
        screeningExpressionUniverse = QuantScreeningExpressionUniverse(
            universe_expr="ISON_DOW", universe_type="Equity", security_expr="TICKER")
        fdsDate = QuantFdsDate(
            start_date="0", end_date="-5D", frequency="D", calendar="FIVEDAY")
        screeningExpression = [QuantScreeningExpression(
            expr="P_PRICE", name="Price (SCR)")]
        fqlExpression = [QuantFqlExpression(
            expr="P_PRICE", name="Price (SCR)")]

        quant_calculation_parameters = {"1": QuantCalculationParameters(screening_expression_universe=screeningExpressionUniverse,
                                        fds_date=fdsDate, screening_expression=screeningExpression, fql_expression=fqlExpression)}

        quant_calculation_parameter_root = QuantCalculationParametersRoot(
            data=quant_calculation_parameters)

        quant_calculations_api = QuantCalculationsApi(api_client)

        post_and_calculate_response = quant_calculations_api.post_and_calculate(
            quant_calculation_parameters_root=quant_calculation_parameter_root, _return_http_data_only=False)

        if post_and_calculate_response[1] == 201:
            output_calculation_result(post_and_calculate_response[0]['data'])
        else:
            calculation_id = post_and_calculate_response[0].data.calculationid
            print("Calculation Id: " + calculation_id)

            status_response = quant_calculations_api.get_calculation_status_by_id(id=calculation_id,
                                                                                  _return_http_data_only=False)

            while status_response[1] == 202 and (status_response[0].data.status in ("Queued", "Executing")):
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = quant_calculations_api.get_calculation_status_by_id(id=calculation_id,
                                                                                      _return_http_data_only=False)

            for (calculation_unit_id, calculation_unit) in status_response[0].data.units.items():
                if calculation_unit.status == "Success":
                    print("Calculation Unit Id: " +
                          calculation_unit_id + " Succeeded!!!")
                    result_response = quant_calculations_api.get_calculation_unit_result_by_id(id=calculation_id,
                                                                                               unit_id=calculation_unit_id,
                                                                                               _return_http_data_only=False)
                    print("Calculation Data")
                    output_calculation_result(result_response[0]['data'])
                    result_response = quant_calculations_api.get_calculation_unit_info_by_id(id=calculation_id,
                                                                                             unit_id=calculation_unit_id,
                                                                                             _return_http_data_only=False)
                    print("Calculation Info")
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
