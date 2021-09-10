import time
import os
from pathlib import Path
import pandas as pd

from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api.quant_calculations_api import QuantCalculationsApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.quant_calculation_parameters_root import QuantCalculationParametersRoot
from fds.analyticsapi.engines.model.quant_calculation_parameters import QuantCalculationParameters
from fds.analyticsapi.engines.model.quant_calculation_meta import QuantCalculationMeta
from fds.analyticsapi.engines.model.quant_identifier_universe import QuantIdentifierUniverse
from fds.analyticsapi.engines.model.quant_fds_date import QuantFdsDate
from fds.analyticsapi.engines.model.quant_screening_expression import QuantScreeningExpression

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

    try:
        identifierUniverse = QuantIdentifierUniverse(source="IdentifierUniverse",
                                                                       universe_type="Equity",
                                                                       identifiers=[
							"IBM",
							"MS",
							"GE"
						])

        fdsDate = QuantFdsDate(source="FdsDate",
            start_date="20050701", end_date="20051001", frequency="M", calendar="FIVEDAY")

        screeningExpression = QuantScreeningExpression(source="ScreeningExpression",
            expr="P_PRICE", name="Price")
        screeningExpression1 = QuantScreeningExpression(source="ScreeningExpression",
            expr="FF_EPS", name="Eps")
        screeningExpression2 = QuantScreeningExpression(source="ScreeningExpression",
            expr="FG_GICS_SECTOR", name="Sector")

        quant_calculation_parameters = {"1": QuantCalculationParameters(
            universe=identifierUniverse,
            dates=fdsDate,
            formulas=[screeningExpression, screeningExpression1, screeningExpression2])
        }

        quant_calculations_meta = QuantCalculationMeta(format='Feather')

        quant_calculation_parameter_root = QuantCalculationParametersRoot(
            data=quant_calculation_parameters, meta=quant_calculations_meta)

        quant_calculations_api = QuantCalculationsApi(api_client)

        post_and_calculate_response = quant_calculations_api.post_and_calculate(
            quant_calculation_parameters_root=quant_calculation_parameter_root)

        if post_and_calculate_response[1] == 201:
            output_calculation_result('data', post_and_calculate_response[0])
        else:
            calculation_id = post_and_calculate_response[0].data.calculationid
            print("Calculation Id: " + calculation_id)

            status_response = quant_calculations_api.get_calculation_status_by_id(id=calculation_id)

            while status_response[1] == 202 and (status_response[0].data.status in ("Queued", "Executing")):
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = quant_calculations_api.get_calculation_status_by_id(id=calculation_id)

            for (calculation_unit_id, calculation_unit) in status_response[0].data.units.items():
                if calculation_unit.status == "Success":
                    print("Calculation Unit Id: " +
                          calculation_unit_id + " Succeeded!!!")
                    result_response = quant_calculations_api.get_calculation_unit_result_by_id(id=calculation_id,
                                                                                               unit_id=calculation_unit_id)
                    print("Calculation Data")
                    output_calculation_result(
                        'data', result_response[0].read())
                    result_response = quant_calculations_api.get_calculation_unit_info_by_id(id=calculation_id,
                                                                                             unit_id=calculation_unit_id)
                    print("Calculation Info")
                    output_calculation_result(
                        'info', result_response[0].read())
                else:
                    print("Calculation Unit Id:" +
                          calculation_unit_id + " Failed!!!")
                    print("Error message : " + str(calculation_unit.errors))

    except ApiException as e:
        print("Api exception Encountered")
        print(e)
        exit()


def output_calculation_result(output_prefix, result):
    filename = Path(f'{output_prefix}-Output.ftr')
    print(f'Writing output to {filename}')
    filename.write_bytes(result)
    df = pd.read_feather(filename)
    print(df)


if __name__ == '__main__':
    main()
