# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from fds.analyticsapi.engines.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from fds.analyticsapi.engines.model.account_directories import AccountDirectories
from fds.analyticsapi.engines.model.axioma_equity_optimization_parameters import AxiomaEquityOptimizationParameters
from fds.analyticsapi.engines.model.calculation import Calculation
from fds.analyticsapi.engines.model.calculation_status import CalculationStatus
from fds.analyticsapi.engines.model.calculation_status_summary import CalculationStatusSummary
from fds.analyticsapi.engines.model.calculation_unit_status import CalculationUnitStatus
from fds.analyticsapi.engines.model.column import Column
from fds.analyticsapi.engines.model.column_statistic import ColumnStatistic
from fds.analyticsapi.engines.model.column_summary import ColumnSummary
from fds.analyticsapi.engines.model.component_account import ComponentAccount
from fds.analyticsapi.engines.model.component_benchmark import ComponentBenchmark
from fds.analyticsapi.engines.model.component_summary import ComponentSummary
from fds.analyticsapi.engines.model.configuration_account import ConfigurationAccount
from fds.analyticsapi.engines.model.currency import Currency
from fds.analyticsapi.engines.model.date_parameters_summary import DateParametersSummary
from fds.analyticsapi.engines.model.document_directories import DocumentDirectories
from fds.analyticsapi.engines.model.event_summary import EventSummary
from fds.analyticsapi.engines.model.fiab_calculation_parameters import FIABCalculationParameters
from fds.analyticsapi.engines.model.fiab_calculation_status import FIABCalculationStatus
from fds.analyticsapi.engines.model.fiab_calculation_status_summary import FIABCalculationStatusSummary
from fds.analyticsapi.engines.model.fiab_date_parameters import FIABDateParameters
from fds.analyticsapi.engines.model.fiab_identifier import FIABIdentifier
from fds.analyticsapi.engines.model.fi_calculation_parameters import FICalculationParameters
from fds.analyticsapi.engines.model.fi_job_settings import FIJobSettings
from fds.analyticsapi.engines.model.fi_security import FISecurity
from fds.analyticsapi.engines.model.frequency import Frequency
from fds.analyticsapi.engines.model.group import Group
from fds.analyticsapi.engines.model.optimal_portfolio import OptimalPortfolio
from fds.analyticsapi.engines.model.optimization import Optimization
from fds.analyticsapi.engines.model.optimizer_account import OptimizerAccount
from fds.analyticsapi.engines.model.optimizer_account_overrides import OptimizerAccountOverrides
from fds.analyticsapi.engines.model.optimizer_optimal_holdings import OptimizerOptimalHoldings
from fds.analyticsapi.engines.model.optimizer_output_types import OptimizerOutputTypes
from fds.analyticsapi.engines.model.optimizer_strategy import OptimizerStrategy
from fds.analyticsapi.engines.model.optimizer_strategy_overrides import OptimizerStrategyOverrides
from fds.analyticsapi.engines.model.optimizer_trades_list import OptimizerTradesList
from fds.analyticsapi.engines.model.pa_calculation_column import PACalculationColumn
from fds.analyticsapi.engines.model.pa_calculation_group import PACalculationGroup
from fds.analyticsapi.engines.model.pa_calculation_parameters import PACalculationParameters
from fds.analyticsapi.engines.model.pa_component import PAComponent
from fds.analyticsapi.engines.model.pa_date_parameters import PADateParameters
from fds.analyticsapi.engines.model.pa_identifier import PAIdentifier
from fds.analyticsapi.engines.model.pub_calculation_parameters import PubCalculationParameters
from fds.analyticsapi.engines.model.pub_date_parameters import PubDateParameters
from fds.analyticsapi.engines.model.pub_identifier import PubIdentifier
from fds.analyticsapi.engines.model.spar_benchmark import SPARBenchmark
from fds.analyticsapi.engines.model.spar_calculation_parameters import SPARCalculationParameters
from fds.analyticsapi.engines.model.spar_date_parameters import SPARDateParameters
from fds.analyticsapi.engines.model.spar_identifier import SPARIdentifier
from fds.analyticsapi.engines.model.vault_calculation_parameters import VaultCalculationParameters
from fds.analyticsapi.engines.model.vault_component import VaultComponent
from fds.analyticsapi.engines.model.vault_configuration import VaultConfiguration
from fds.analyticsapi.engines.model.vault_configuration_summary import VaultConfigurationSummary
from fds.analyticsapi.engines.model.vault_date_parameters import VaultDateParameters
from fds.analyticsapi.engines.model.vault_identifier import VaultIdentifier
