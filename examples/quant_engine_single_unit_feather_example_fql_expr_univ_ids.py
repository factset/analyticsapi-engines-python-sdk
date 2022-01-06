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
from fds.analyticsapi.engines.model.quant_screening_expression_universe import QuantScreeningExpressionUniverse
from fds.analyticsapi.engines.model.quant_identifier_universe import QuantIdentifierUniverse
from fds.analyticsapi.engines.model.quant_fds_date import QuantFdsDate
from fds.analyticsapi.engines.model.quant_screening_expression import QuantScreeningExpression
from fds.analyticsapi.engines.model.quant_fql_expression import QuantFqlExpression
from fds.analyticsapi.engines.model.quant_all_universal_screen_parameters import QuantAllUniversalScreenParameters

from urllib3 import Retry

host = os.environ['FACTSET_HOST']
fds_username = os.environ['FACTSET_USERNAME']
fds_api_key = os.environ['FACTSET_API_KEY']


def main():
    config = Configuration()
    config.host = host
    config.username = fds_username
    config.password = fds_api_key
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
            start_date="20050701", end_date="20051001", frequency="M", calendar="SEVENDAY")

        fqlExpression = QuantFqlExpression(source="FqlExpression",
            expr="P_PRICE(#DATE,#DATE,#FREQ)", name="Price")
        fqlExpression1 = QuantFqlExpression(source="FqlExpression",
            expr="FF_EPS(,#DATE,#DATE,#FREQ)", name="Eps")
        fqlExpression2 = QuantFqlExpression(source="FqlExpression",
            expr="FG_GICS_SECTOR", name="Sector")
        # uncomment the below code line to setup cache control; max-stale=0 will be a fresh adhoc run and the max-stale value is in seconds.
        # Results are by default cached for 12 hours; Setting max-stale=300 will fetch a cached result which is 5 minutes older. 
        # cache_control = "max-stale=0"
        quant_calculation_parameters = {"1": QuantCalculationParameters(
            universe=identifierUniverse,
            dates=fdsDate,
            formulas=[fqlExpression, fqlExpression1, fqlExpression2])
        }

        quant_calculations_meta = QuantCalculationMeta(format='Feather')

        quant_calculation_parameter_root = QuantCalculationParametersRoot(
            data=quant_calculation_parameters, meta=quant_calculations_meta)

        quant_calculations_api = QuantCalculationsApi(api_client)

        post_and_calculate_response = quant_calculations_api.post_and_calculate(
            quant_calculation_parameters_root=quant_calculation_parameter_root)
        # comment the above line and uncomment the below line to run the request with the cache_control header defined earlier
        # post_and_calculate_response = quant_calculations_api.post_and_calculate(
            # quant_calculation_parameters_root=quant_calculation_parameter_root, cache_control=cache_control)
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
