import time
import os
import uuid
import pandas as pd
import json
import urllib3
from fds.analyticsapi.engines import ApiException
from fds.analyticsapi.engines.api.fiab_calculations_api import FIABCalculationsApi
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.model.fiab_calculation_parameters import FIABCalculationParameters
from fds.analyticsapi.engines.model.fiab_calculation_status_summary import FIABCalculationStatusSummary
from fds.analyticsapi.engines.model.fiab_calculation_status import FIABCalculationStatus
from fds.analyticsapi.engines.model.fiab_date_parameters import FIABDateParameters
from fds.analyticsapi.engines.model.fiab_identifier import FIABIdentifier
from urllib3 import Retry

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

fds_username = os.environ['FACTSET_USERNAME']
fds_api_key = os.environ['FACTSET_API_KEY']
host = os.environ['FACTSET_HOST']


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
    fiab_calculations_api = FIABCalculationsApi(api_client)
    
    try:
        fiab_document_name = "Client:FIAB_EXPO_DEMO"
        faccount = "CLIENT:/Test46238.ACCT"
        startdate = "20200101"
        enddate = "20201213"
        fiab_account = FIABIdentifier(id=faccount)
        fiab_dates = FIABDateParameters(startdate=startdate, enddate=enddate)
        fiab_calculation_parameters = FIABCalculationParameters(fiabdocument=fiab_document_name, account=fiab_account, dates=fiab_dates)
    
        run_calculation = fiab_calculations_api.run_calculation(fiab_calculation_parameters=fiab_calculation_parameters)
        if run_calculation[1] == 202:
            calculation_id = run_calculation[2]['X-FactSet-Api-Calculation-Id']
            print(calculation_id)
            status_response = fiab_calculations_api.get_calculation_by_id(calculation_id)
            while status_response[1] == 202:
                max_age = '5'
                age_value = status_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                print('Calculation status is', status_response[0]['status'])
                #print('Sleeping: ' + max_age)
                if(status_response[0]['status']) == 'Pending':
                    print(status_response)
                if(status_response[0]['progress']!=0):
                   print(status_response[0])
                time.sleep(int(max_age))
                status_response = fiab_calculations_api.get_calculation_by_id(calculation_id)
            if status_response[1] == 200:
                print(status_response)
            print(status_response)
            
    except ApiException as e:
        print("Api exception Encountered")
        print(e)


if __name__ == '__main__':
    main()
