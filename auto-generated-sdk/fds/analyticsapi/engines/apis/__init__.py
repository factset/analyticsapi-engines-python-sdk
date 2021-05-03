
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.accounts_api import AccountsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from fds.analyticsapi.engines.api.accounts_api import AccountsApi
from fds.analyticsapi.engines.api.calculations_api import CalculationsApi
from fds.analyticsapi.engines.api.column_statistics_api import ColumnStatisticsApi
from fds.analyticsapi.engines.api.columns_api import ColumnsApi
from fds.analyticsapi.engines.api.components_api import ComponentsApi
from fds.analyticsapi.engines.api.configurations_api import ConfigurationsApi
from fds.analyticsapi.engines.api.currencies_api import CurrenciesApi
from fds.analyticsapi.engines.api.dates_api import DatesApi
from fds.analyticsapi.engines.api.documents_api import DocumentsApi
from fds.analyticsapi.engines.api.fiab_calculations_api import FIABCalculationsApi
from fds.analyticsapi.engines.api.fi_calculations_api import FICalculationsApi
from fds.analyticsapi.engines.api.frequencies_api import FrequenciesApi
from fds.analyticsapi.engines.api.groups_api import GroupsApi
from fds.analyticsapi.engines.api.optimizations_api import OptimizationsApi
from fds.analyticsapi.engines.api.pa_calculations_api import PACalculationsApi
from fds.analyticsapi.engines.api.spar_benchmark_api import SPARBenchmarkApi
from fds.analyticsapi.engines.api.spar_calculations_api import SPARCalculationsApi
from fds.analyticsapi.engines.api.strategy_documents_api import StrategyDocumentsApi
from fds.analyticsapi.engines.api.vault_calculations_api import VaultCalculationsApi
