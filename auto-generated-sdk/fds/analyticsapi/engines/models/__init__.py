# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from fds.analyticsapi.engines.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from fds.analyticsapi.engines.model.afi_optimization_parameters import AFIOptimizationParameters
from fds.analyticsapi.engines.model.afi_optimization_parameters_root import AFIOptimizationParametersRoot
from fds.analyticsapi.engines.model.afi_optimizer_strategy import AFIOptimizerStrategy
from fds.analyticsapi.engines.model.afi_optimizer_strategy_overrides import AFIOptimizerStrategyOverrides
from fds.analyticsapi.engines.model.account_directories import AccountDirectories
from fds.analyticsapi.engines.model.account_directories_root import AccountDirectoriesRoot
from fds.analyticsapi.engines.model.axioma_equity_optimization_parameters import AxiomaEquityOptimizationParameters
from fds.analyticsapi.engines.model.axioma_equity_optimization_parameters_root import AxiomaEquityOptimizationParametersRoot
from fds.analyticsapi.engines.model.axioma_equity_optimizer_strategy import AxiomaEquityOptimizerStrategy
from fds.analyticsapi.engines.model.axioma_equity_optimizer_strategy_overrides import AxiomaEquityOptimizerStrategyOverrides
from fds.analyticsapi.engines.model.bpm_optimization import BPMOptimization
from fds.analyticsapi.engines.model.bpm_optimization_parameters import BPMOptimizationParameters
from fds.analyticsapi.engines.model.bpm_optimization_parameters_root import BPMOptimizationParametersRoot
from fds.analyticsapi.engines.model.bpm_optimizer_strategy import BPMOptimizerStrategy
from fds.analyticsapi.engines.model.bpm_optimizer_strategy_alpha_override import BPMOptimizerStrategyAlphaOverride
from fds.analyticsapi.engines.model.bpm_optimizer_strategy_overrides import BPMOptimizerStrategyOverrides
from fds.analyticsapi.engines.model.calculation_info import CalculationInfo
from fds.analyticsapi.engines.model.calculation_info_root import CalculationInfoRoot
from fds.analyticsapi.engines.model.calculation_meta import CalculationMeta
from fds.analyticsapi.engines.model.calculation_status import CalculationStatus
from fds.analyticsapi.engines.model.calculation_status_meta import CalculationStatusMeta
from fds.analyticsapi.engines.model.calculation_status_root import CalculationStatusRoot
from fds.analyticsapi.engines.model.calculation_unit_status import CalculationUnitStatus
from fds.analyticsapi.engines.model.calculation_unit_status_meta import CalculationUnitStatusMeta
from fds.analyticsapi.engines.model.client_error_response import ClientErrorResponse
from fds.analyticsapi.engines.model.column import Column
from fds.analyticsapi.engines.model.column_root import ColumnRoot
from fds.analyticsapi.engines.model.column_statistic import ColumnStatistic
from fds.analyticsapi.engines.model.column_statistic_root import ColumnStatisticRoot
from fds.analyticsapi.engines.model.column_summary import ColumnSummary
from fds.analyticsapi.engines.model.column_summary_root import ColumnSummaryRoot
from fds.analyticsapi.engines.model.component_summary import ComponentSummary
from fds.analyticsapi.engines.model.component_summary_root import ComponentSummaryRoot
from fds.analyticsapi.engines.model.configuration_account import ConfigurationAccount
from fds.analyticsapi.engines.model.constraint_action import ConstraintAction
from fds.analyticsapi.engines.model.currency import Currency
from fds.analyticsapi.engines.model.currency_root import CurrencyRoot
from fds.analyticsapi.engines.model.date_parameters_summary import DateParametersSummary
from fds.analyticsapi.engines.model.date_parameters_summary_root import DateParametersSummaryRoot
from fds.analyticsapi.engines.model.document_directories import DocumentDirectories
from fds.analyticsapi.engines.model.document_directories_root import DocumentDirectoriesRoot
from fds.analyticsapi.engines.model.error import Error
from fds.analyticsapi.engines.model.error_source import ErrorSource
from fds.analyticsapi.engines.model.event_summary import EventSummary
from fds.analyticsapi.engines.model.fiab_calculation_parameters import FIABCalculationParameters
from fds.analyticsapi.engines.model.fiab_calculation_status import FIABCalculationStatus
from fds.analyticsapi.engines.model.fiab_calculation_status_summary import FIABCalculationStatusSummary
from fds.analyticsapi.engines.model.fiab_date_parameters import FIABDateParameters
from fds.analyticsapi.engines.model.fiab_identifier import FIABIdentifier
from fds.analyticsapi.engines.model.fi_calculation_parameters import FICalculationParameters
from fds.analyticsapi.engines.model.fi_calculation_parameters_root import FICalculationParametersRoot
from fds.analyticsapi.engines.model.fi_job_settings import FIJobSettings
from fds.analyticsapi.engines.model.fi_security import FISecurity
from fds.analyticsapi.engines.model.fpo_account import FPOAccount
from fds.analyticsapi.engines.model.fpo_optimization_parameters import FPOOptimizationParameters
from fds.analyticsapi.engines.model.fpo_optimization_parameters_root import FPOOptimizationParametersRoot
from fds.analyticsapi.engines.model.frequency import Frequency
from fds.analyticsapi.engines.model.frequency_root import FrequencyRoot
from fds.analyticsapi.engines.model.group import Group
from fds.analyticsapi.engines.model.group_root import GroupRoot
from fds.analyticsapi.engines.model.linked_pa_template import LinkedPATemplate
from fds.analyticsapi.engines.model.linked_pa_template_parameters import LinkedPATemplateParameters
from fds.analyticsapi.engines.model.linked_pa_template_parameters_root import LinkedPATemplateParametersRoot
from fds.analyticsapi.engines.model.linked_pa_template_root import LinkedPATemplateRoot
from fds.analyticsapi.engines.model.linked_pa_template_summary import LinkedPATemplateSummary
from fds.analyticsapi.engines.model.linked_pa_template_summary_root import LinkedPATemplateSummaryRoot
from fds.analyticsapi.engines.model.linked_pa_template_update_parameters import LinkedPATemplateUpdateParameters
from fds.analyticsapi.engines.model.linked_pa_template_update_parameters_root import LinkedPATemplateUpdateParametersRoot
from fds.analyticsapi.engines.model.npo_optimization_parameters import NPOOptimizationParameters
from fds.analyticsapi.engines.model.npo_optimization_parameters_root import NPOOptimizationParametersRoot
from fds.analyticsapi.engines.model.npo_optimizer_strategy import NPOOptimizerStrategy
from fds.analyticsapi.engines.model.npo_optimizer_strategy_overrides import NPOOptimizerStrategyOverrides
from fds.analyticsapi.engines.model.object_root import ObjectRoot
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
from fds.analyticsapi.engines.model.pa_calculation_parameters_root import PACalculationParametersRoot
from fds.analyticsapi.engines.model.pa_component import PAComponent
from fds.analyticsapi.engines.model.pa_component_data import PAComponentData
from fds.analyticsapi.engines.model.pa_component_root import PAComponentRoot
from fds.analyticsapi.engines.model.pa_date_parameters import PADateParameters
from fds.analyticsapi.engines.model.pa_identifier import PAIdentifier
from fds.analyticsapi.engines.model.pa_doc import PaDoc
from fds.analyticsapi.engines.model.pub_calculation_parameters import PubCalculationParameters
from fds.analyticsapi.engines.model.pub_calculation_parameters_root import PubCalculationParametersRoot
from fds.analyticsapi.engines.model.pub_date_parameters import PubDateParameters
from fds.analyticsapi.engines.model.pub_identifier import PubIdentifier
from fds.analyticsapi.engines.model.quant_all_universal_screen_parameters import QuantAllUniversalScreenParameters
from fds.analyticsapi.engines.model.quant_calculation_meta import QuantCalculationMeta
from fds.analyticsapi.engines.model.quant_calculation_parameters import QuantCalculationParameters
from fds.analyticsapi.engines.model.quant_calculation_parameters_root import QuantCalculationParametersRoot
from fds.analyticsapi.engines.model.quant_date import QuantDate
from fds.analyticsapi.engines.model.quant_date_list import QuantDateList
from fds.analyticsapi.engines.model.quant_date_list1 import QuantDateList1
from fds.analyticsapi.engines.model.quant_date_list_all_of import QuantDateListAllOf
from fds.analyticsapi.engines.model.quant_fds_date import QuantFdsDate
from fds.analyticsapi.engines.model.quant_fds_date1 import QuantFdsDate1
from fds.analyticsapi.engines.model.quant_fds_date_all_of import QuantFdsDateAllOf
from fds.analyticsapi.engines.model.quant_formula import QuantFormula
from fds.analyticsapi.engines.model.quant_fql_expression import QuantFqlExpression
from fds.analyticsapi.engines.model.quant_fql_expression1 import QuantFqlExpression1
from fds.analyticsapi.engines.model.quant_identifier_universe import QuantIdentifierUniverse
from fds.analyticsapi.engines.model.quant_identifier_universe1 import QuantIdentifierUniverse1
from fds.analyticsapi.engines.model.quant_identifier_universe_all_of import QuantIdentifierUniverseAllOf
from fds.analyticsapi.engines.model.quant_screening_expression import QuantScreeningExpression
from fds.analyticsapi.engines.model.quant_screening_expression1 import QuantScreeningExpression1
from fds.analyticsapi.engines.model.quant_screening_expression_all_of import QuantScreeningExpressionAllOf
from fds.analyticsapi.engines.model.quant_screening_expression_universe import QuantScreeningExpressionUniverse
from fds.analyticsapi.engines.model.quant_screening_expression_universe1 import QuantScreeningExpressionUniverse1
from fds.analyticsapi.engines.model.quant_screening_expression_universe_all_of import QuantScreeningExpressionUniverseAllOf
from fds.analyticsapi.engines.model.quant_universal_screen_parameter import QuantUniversalScreenParameter
from fds.analyticsapi.engines.model.quant_universal_screen_parameter1 import QuantUniversalScreenParameter1
from fds.analyticsapi.engines.model.quant_universal_screen_parameter_all_of import QuantUniversalScreenParameterAllOf
from fds.analyticsapi.engines.model.quant_universal_screen_universe import QuantUniversalScreenUniverse
from fds.analyticsapi.engines.model.quant_universal_screen_universe1 import QuantUniversalScreenUniverse1
from fds.analyticsapi.engines.model.quant_universal_screen_universe_all_of import QuantUniversalScreenUniverseAllOf
from fds.analyticsapi.engines.model.quant_universe import QuantUniverse
from fds.analyticsapi.engines.model.return_type import ReturnType
from fds.analyticsapi.engines.model.spar_accounts import SPARAccounts
from fds.analyticsapi.engines.model.spar_accounts_root import SPARAccountsRoot
from fds.analyticsapi.engines.model.spar_benchmark import SPARBenchmark
from fds.analyticsapi.engines.model.spar_benchmark_root import SPARBenchmarkRoot
from fds.analyticsapi.engines.model.spar_calculation_parameters import SPARCalculationParameters
from fds.analyticsapi.engines.model.spar_calculation_parameters_root import SPARCalculationParametersRoot
from fds.analyticsapi.engines.model.spar_date_parameters import SPARDateParameters
from fds.analyticsapi.engines.model.spar_identifier import SPARIdentifier
from fds.analyticsapi.engines.model.template_content_types import TemplateContentTypes
from fds.analyticsapi.engines.model.templated_pa_component_parameters import TemplatedPAComponentParameters
from fds.analyticsapi.engines.model.templated_pa_component_parameters_root import TemplatedPAComponentParametersRoot
from fds.analyticsapi.engines.model.templated_pa_component_summary import TemplatedPAComponentSummary
from fds.analyticsapi.engines.model.templated_pa_component_summary_root import TemplatedPAComponentSummaryRoot
from fds.analyticsapi.engines.model.templated_pa_component_update_parameters import TemplatedPAComponentUpdateParameters
from fds.analyticsapi.engines.model.templated_pa_component_update_parameters_root import TemplatedPAComponentUpdateParametersRoot
from fds.analyticsapi.engines.model.unlinked_pa_template import UnlinkedPATemplate
from fds.analyticsapi.engines.model.unlinked_pa_template_category_and_type import UnlinkedPATemplateCategoryAndType
from fds.analyticsapi.engines.model.unlinked_pa_template_category_and_type_details import UnlinkedPATemplateCategoryAndTypeDetails
from fds.analyticsapi.engines.model.unlinked_pa_template_category_and_type_details_root import UnlinkedPATemplateCategoryAndTypeDetailsRoot
from fds.analyticsapi.engines.model.unlinked_pa_template_category_and_type_root import UnlinkedPATemplateCategoryAndTypeRoot
from fds.analyticsapi.engines.model.unlinked_pa_template_parameters import UnlinkedPATemplateParameters
from fds.analyticsapi.engines.model.unlinked_pa_template_parameters_root import UnlinkedPATemplateParametersRoot
from fds.analyticsapi.engines.model.unlinked_pa_template_root import UnlinkedPATemplateRoot
from fds.analyticsapi.engines.model.unlinked_pa_template_summary import UnlinkedPATemplateSummary
from fds.analyticsapi.engines.model.unlinked_pa_template_summary_root import UnlinkedPATemplateSummaryRoot
from fds.analyticsapi.engines.model.unlinked_pa_template_update_parameters import UnlinkedPATemplateUpdateParameters
from fds.analyticsapi.engines.model.unlinked_pa_template_update_parameters_root import UnlinkedPATemplateUpdateParametersRoot
from fds.analyticsapi.engines.model.vault_calculation_parameters import VaultCalculationParameters
from fds.analyticsapi.engines.model.vault_calculation_parameters_root import VaultCalculationParametersRoot
from fds.analyticsapi.engines.model.vault_component import VaultComponent
from fds.analyticsapi.engines.model.vault_component_root import VaultComponentRoot
from fds.analyticsapi.engines.model.vault_configuration import VaultConfiguration
from fds.analyticsapi.engines.model.vault_configuration_root import VaultConfigurationRoot
from fds.analyticsapi.engines.model.vault_configuration_summary import VaultConfigurationSummary
from fds.analyticsapi.engines.model.vault_configuration_summary_root import VaultConfigurationSummaryRoot
from fds.analyticsapi.engines.model.vault_date_parameters import VaultDateParameters
from fds.analyticsapi.engines.model.vault_identifier import VaultIdentifier
