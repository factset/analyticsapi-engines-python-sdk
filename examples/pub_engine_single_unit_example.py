import os
import time
from pathlib import Path

import urllib3
from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.api.pub_calculations_api import PubCalculationsApi
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.pub_calculation_parameters import PubCalculationParameters
from fds.analyticsapi.engines.model.pub_calculation_parameters_root import PubCalculationParametersRoot
from fds.analyticsapi.engines.model.pub_identifier import PubIdentifier
from fds.analyticsapi.engines.model.pub_date_parameters import PubDateParameters

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

    try:
        pub_document_name = "Super_client:/publisher/Equity Snapshot.PUB_BRIDGE_PDF"
        pub_account_id = "BENCH:SP50"
        startdate = "-1M"
        enddate = "0M"
        # uncomment the below code line to setup cache control; max-stale=0 will be a fresh adhoc run and the max-stale value is in seconds.
        # Results are by default cached for 12 hours; Setting max-stale=300 will fetch a cached result which is 5 minutes older.
        # cache_control = "max-stale=0"
        pub_account_identifier = PubIdentifier(pub_account_id)
        pub_dates = PubDateParameters(enddate, startdate=startdate)

        pub_calculation_parameters = {
            "1": PubCalculationParameters(pub_document_name, pub_account_identifier, pub_dates)
        }

        pub_calculation_parameters_root = PubCalculationParametersRoot(
            data=pub_calculation_parameters)

        pub_calculations_api = PubCalculationsApi(api_client)
        post_and_calculate_response = pub_calculations_api.post_and_calculate(
           pub_calculation_parameters_root=pub_calculation_parameters_root)
        # comment the above line and uncomment the below line to run the request with the cache_control header defined earlier
        # post_and_calculate_response = pub_calculations_api.post_and_calculate(pub_calculation_parameters_root=pub_calculation_parameters_root, cache_control=cache_control)
        if post_and_calculate_response[1] == 201:
            output_calculation_result(
                "single_unit", (post_and_calculate_response[0].read()))
        elif post_and_calculate_response[1] == 200:
            for (calculation_unit_id, calculation_unit) in post_and_calculate_response[0].data.units.items():
                print("Calculation Unit Id:" +
                      calculation_unit_id + " Failed!!!")
                print("Error message : " + str(calculation_unit.errors))
        else:
            calculation_id = post_and_calculate_response[0].data.calculationid
            print("Calculation Id: " + calculation_id)

            status_response = pub_calculations_api.get_calculation_status_by_id(id=calculation_id)

            while status_response[1] == 202 and (status_response[0].data.status in ("Queued", "Executing")):
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Sleeping: ' + max_age)
                time.sleep(int(max_age))
                status_response = pub_calculations_api.get_calculation_status_by_id(calculation_id)

            for (calculation_unit_id, calculation_unit) in status_response[0].data.units.items():
                if calculation_unit.status == "Success":
                    print("Calculation Unit Id: " +
                          calculation_unit_id + " Succeeded!!!")
                    result_response = pub_calculations_api.get_calculation_unit_result_by_id(id=calculation_id,
                                                                                             unit_id=calculation_unit_id)

                    output_calculation_result(
                        "single_unit", (result_response[0].read()))
                else:
                    print("Calculation Unit Id:" +
                          calculation_unit_id + " Failed!!!")
                    print("Error message : " + str(calculation_unit.errors))

    except ApiException as e:
        print("Api exception Encountered")
        print(e)
        exit()


def output_calculation_result(output_prefix, result):
    filename = Path(f'{output_prefix}-Output.pdf')
    print(f'Writing output to {filename}')
    filename.write_bytes(result)


if __name__ == '__main__':
    main()
