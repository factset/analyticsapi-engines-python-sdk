
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.afi_optimizer_api import AFIOptimizerApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from fds.analyticsapi.engines.api.afi_optimizer_api import AFIOptimizerApi
from fds.analyticsapi.engines.api.axp_optimizer_api import AXPOptimizerApi
from fds.analyticsapi.engines.api.accounts_api import AccountsApi
from fds.analyticsapi.engines.api.bpm_optimizer_api import BPMOptimizerApi
from fds.analyticsapi.engines.api.benchmarks_api import BenchmarksApi
from fds.analyticsapi.engines.api.column_statistics_api import ColumnStatisticsApi
from fds.analyticsapi.engines.api.columns_api import ColumnsApi
from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.api.configurations_api import ConfigurationsApi
from fds.analyticsapi.engines.api.currencies_api import CurrenciesApi
from fds.analyticsapi.engines.api.dates_api import DatesApi
from fds.analyticsapi.engines.api.discount_curves_api import DiscountCurvesApi
from fds.analyticsapi.engines.api.documents_api import DocumentsApi
from fds.analyticsapi.engines.api.fiab_calculations_api import FIABCalculationsApi
from fds.analyticsapi.engines.api.fi_calculations_api import FICalculationsApi
from fds.analyticsapi.engines.api.fpo_optimizer_api import FPOOptimizerApi
from fds.analyticsapi.engines.api.frequencies_api import FrequenciesApi
from fds.analyticsapi.engines.api.groups_api import GroupsApi
from fds.analyticsapi.engines.api.linked_pa_templates_api import LinkedPATemplatesApi
from fds.analyticsapi.engines.api.npo_optimizer_api import NPOOptimizerApi
from fds.analyticsapi.engines.api.pa_calculations_api import PACalculationsApi
from fds.analyticsapi.engines.api.pricing_sources_api import PricingSourcesApi
from fds.analyticsapi.engines.api.pub_calculations_api import PubCalculationsApi
from fds.analyticsapi.engines.api.quant_calculations_api import QuantCalculationsApi
from fds.analyticsapi.engines.api.spar_calculations_api import SPARCalculationsApi
from fds.analyticsapi.engines.api.strategy_documents_api import StrategyDocumentsApi
from fds.analyticsapi.engines.api.templated_pa_components_api import TemplatedPAComponentsApi
from fds.analyticsapi.engines.api.unlinked_pa_templates_api import UnlinkedPATemplatesApi
from fds.analyticsapi.engines.api.vault_calculations_api import VaultCalculationsApi
