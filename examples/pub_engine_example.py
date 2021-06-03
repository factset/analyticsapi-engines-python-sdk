import json
import sys
import time

from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.pub_calculations_api import PubCalculationsApi
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.pub_calculation_parameters import PubCalculationParameters
from fds.analyticsapi.engines.model.pub_calculation_parameters_root import PubCalculationParametersRoot
from fds.analyticsapi.engines.model.pub_identifier import PubIdentifier
from fds.analyticsapi.engines.model.pub_date_parameters import PubDateParameters

from urllib3 import Retry
from pathlib import Path

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
        pub_document_name = "Super_client:/publisher/Equity Snapshot.PUB_BRIDGE_PDF"
        pub_account_name = "BENCH:SP50"
        startdate = "-1M"
        enddate = "0M"

        pub_account_identifier = PubIdentifier(pub_account_name)
        pub_dates = PubDateParameters(startdate, enddate)

        pub_calculation_parameters = {
            "1": PubCalculationParameters(pub_document_name, pub_account_identifier, pub_dates)}

        calculation = Calculation(pub=pub_calculation_parameters)

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

        for (calculation_unit, calculation_unit_id) in zip(status_response[0].pub.values(), status_response[0].pub):
            if calculation_unit.status == "Success":
                print("Calculation Unit Id: " + calculation_unit_id + " Succeeded!!!")
                utility_api = UtilityApi(api_client)
                result_response = utility_api.get_by_url_with_http_info(calculation_unit.result, _preload_content=False)

                print("Calculation Succeeded")
                filename = Path('Output.pdf')
                filename.write_bytes(result_response[0].data)
            else:
                print("Calculation Unit Id:" + calculation_unit_id + " Failed!!!")
                print("Error message : " + calculation_unit.error)

    except ApiException as e:
        print("Api exception Encountered")
        print(e)
        exit()


if __name__ == '__main__':
    main()
