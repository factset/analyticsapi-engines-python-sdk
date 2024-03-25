import time
import unittest

from fds.analyticsapi.engines.api.fi_calculations_api import FICalculationsApi
from fds.analyticsapi.engines.model.fi_calculation_parameters import FICalculationParameters
from fds.analyticsapi.engines.model.fi_calculation_parameters_root import FICalculationParametersRoot
from fds.analyticsapi.engines.model.fi_security import FISecurity
from fds.analyticsapi.engines.model.fi_job_settings import FIJobSettings
from fds.analyticsapi.engines.model.fi_bank_loans import FIBankLoans
from fds.analyticsapi.engines.model.fi_municipal_bonds import FIMunicipalBonds
from fds.analyticsapi.engines.model.fi_municipal_bonds_for_job_settings import FIMunicipalBondsForJobSettings
from fds.analyticsapi.engines.model.fi_attribution_for_securities import FIAttributionForSecurities
from fds.analyticsapi.engines.model.fi_attribution_for_job_settings import FIAttributionForJobSettings

import common_parameters
from common_functions import CommonFunctions


class TestFICalculationsApi(unittest.TestCase):
    def setUp(self):
        self.api_client = CommonFunctions.build_api_client()
        self.calculations_api = FICalculationsApi(self.api_client)
        self.run_response = self.run_calculation()
        self.status_response = None

    def run_calculation(self):
        calculations = ["Security Type",
                        "Security Name",
                        "Run Status",
                        "Elapse Time (seconds)",
                        "Calc From Method",
                        "Option Pricing Model",
                        "Yield Curve Date",
                        "Settlement Date",
                        "Discount Curve",
                        "Price",
                        "Yield to No Call",
                        "OAS",
                        "Effective Duration",
                        "Effective Convexity"]

        securities = [
            FISecurity(calc_from_method="Price",
                       calc_from_value=100.285,
                       symbol="912828ZG8",
                       settlement="20201202",
                       discount_curve="UST",
                       face=10000.0,
                       bank_loans=FIBankLoans(ignore_sinking_fund=True),
                       municipal_bonds=FIMunicipalBonds(ignore_sinking_fund=True),
                       attribution=FIAttributionForSecurities(start_price=100.00, end_price=100.3668,
                                                              pricing_method="Inputted Price")
                       ),
            FISecurity(calc_from_method="Price",
                       calc_from_value=101.138,
                       symbol="US037833AR12",
                       settlement="20201203",
                       discount_curve="UST",
                       face=200000.0,
                       bank_loans=FIBankLoans(ignore_sinking_fund=True),
                       municipal_bonds=FIMunicipalBonds(ignore_sinking_fund=True),
                       attribution=FIAttributionForSecurities(start_price=100.00, end_price=100.3668,
                                                              pricing_method="Inputted Price")
                       )
        ]

        jobSettings = FIJobSettings(as_of_date="20201201",
                                    bank_loans=FIBankLoans(ignore_sinking_fund=True),
                                    municipal_bonds=FIMunicipalBondsForJobSettings(ignore_sinking_fund=True),
                                    attribution=FIAttributionForJobSettings(start_date="20210611", end_date="20210611"))

        fi_calculation_parameters = FICalculationParameters(
            securities, calculations, jobSettings)
        fi_calculation_parameters_root = FICalculationParametersRoot(
            data=fi_calculation_parameters)

        return self.calculations_api.post_and_calculate(
            fi_calculation_parameters_root=fi_calculation_parameters_root,
            _return_http_data_only=False
        )

    def test_calculation_success(self):
        if self.run_response[1] == 202:
            calculation_id = self.run_response[2]["X-Factset-Api-Calculation-Id"]
            self.run_response = self.calculations_api.get_calculation_status_by_id(
                id=calculation_id, _return_http_data_only=False)
            while self.run_response[1] == 202:
                age_value = self.run_response[2].get("cache-control")
                if age_value is not None:
                    max_age = age_value.replace("max-age=", "")
                    time.sleep(int(max_age))
                else:
                    time.sleep(5)
                self.run_response = self.calculations_api.get_calculation_status_by_id(
                    id=calculation_id, _return_http_data_only=False)

        self.assertTrue(
            self.run_response[1] == 200 or self.run_response[1] == 201, "Calculation should be completed")


if __name__ == '__main__':
    unittest.main()
