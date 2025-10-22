import os

# Set 'ANALYTICS_API_QAR_USERNAME_SERIAL' environment variable with username-serial as value
user_name = os.getenv("ANALYTICS_API_QAR_USERNAME_SERIAL")
# Set 'ANALYTICS_API_QAR_PASSWORD' environment variable with the api key generated on developer portal
password = os.getenv("ANALYTICS_API_QAR_PASSWORD")

# Set 'ANALYTICS_API_URL' environment variable with api url as value
base_url = 'https://api.factset.com' if not os.getenv("ANALYTICS_API_URL") else os.getenv("ANALYTICS_API_URL")

pa_default_document = "PA3_DOCUMENTS:PA_API_DEFAULT_DOCUMENT-RBICS"
pa_default_component_name = "Weights"
pa_default_component_category = "Weights / Exposures"
pa_benchmark_sp500 = "BENCH:SP50"
pa_benchmark_r1000 = "BENCH:R.1000"
spar_default_document = "pmw_root:/spar_documents/Factset Default Document"
spar_benchmark_r1000 = "R.1000"
spar_benchmark_r2000 = "R.2000"
spar_benchmark_russell_p_r1000 = "RUSSELL_P:R.2000"
spar_benchmark_russell_prefix = "RUSSELL"
spar_benchmark_russell_return_type = "GTR"
vault_default_document = "CLIENT:/YETI/YETI-API-TEST"
vault_default_account = "CLIENT:/YETI/YETI-API-TEST.ACCT"
vault_start_date = "20211231"
vault_end_date = "20220131"
pub_document_name = "Client:/AAPI/Puma Narrative Test.PUB_BRIDGE_PDF"
pub_account_name = "BENCH:SP50"
pub_start_date = "-1M"
pub_end_date = "0M"
default_start_date = "20180101"
default_end_date = "20181231"
default_dates_frequency = "Monthly"
default_dates_account = "CLIENT:/BISAM/REPOSITORY/QA/SMALL_PORT.ACCT"
default_lookup_directory = "client:"
# This is exclusively created for the quant tests to avoid frequent status calls
quant_max_age = '5' if not os.getenv("QUANT_CUSTOM_MAX_AGE") else os.getenv("QUANT_CUSTOM_MAX_AGE")
spar_account = "client:/aapi/spar3_qa_test_document"
