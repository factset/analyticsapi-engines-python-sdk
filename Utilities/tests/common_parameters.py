import os

# Set 'ANALYTICS_API_USERNAME_SERIAL' environment variable with username-serial as value
user_name = os.getenv("ANALYTICS_API_USERNAME_SERIAL")
# Set 'ANALYTICS_API_PASSWORD' environment variable with the api key generated on developer portal
password = os.getenv("ANALYTICS_API_PASSWORD")

# Set 'ANALYTICS_API_URL' environment variable with api url as value
base_url = 'https://api.factset.com' if not os.getenv("ANALYTICS_API_URL") else os.getenv("ANALYTICS_API_URL")

pa_default_document = "PA_DOCUMENTS:DEFAULT"
pa_benchmark_sp500 = "BENCH:SP50"
pa_benchmark_r1000 = "BENCH:R.1000"
spar_default_document = "pmw_root:/spar_documents/Factset Default Document"
spar_benchmark_r1000 = "R.1000"
spar_benchmark_r2000 = "R.2000"
spar_benchmark_russell_p_r1000 = "RUSSELL_P:R.2000"
spar_benchmark_russell_prefix = "RUSSELL"
spar_benchmark_russell_return_type = "GTR"
vault_default_document = "PA3_DOCUMENTS:DEFAULT"
vault_default_account = "Client:/analytics/data/US_MID_CAP_CORE.ACTM"
vault_start_date = "FIRST_REPOSITORY"
vault_end_date = "LAST_REPOSITORY"
pub_document_name = "Super_client:/publisher/Equity Snapshot.PUB_BRIDGE_PDF"
pub_account_name = "BENCH:SP50"
pub_start_date = "-1M"
pub_end_date = "0M"
default_start_date = "20180101"
default_end_date = "20181231"
default_dates_frequency = "Monthly"
default_dates_account = "Client:/analytics/data/US_MID_CAP_CORE.ACTM"
default_lookup_directory = "client:"
