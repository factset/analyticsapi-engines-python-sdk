
# fds.analyticsapi.engines.SecurityModelingApi

All URIs are relative to *https://api.factset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_securities**](SecurityModelingApi.md#delete_securities) | **POST** /analytics/security-modeling/v3/securities/delete | Delete existing securities
[**get_securities**](SecurityModelingApi.md#get_securities) | **POST** /analytics/security-modeling/v3/securities/retrieve | Get existing securities
[**get_template_fields**](SecurityModelingApi.md#get_template_fields) | **GET** /analytics/security-modeling/v3/templates/{template}/fields | Get template fields
[**upsert_securities**](SecurityModelingApi.md#upsert_securities) | **POST** /analytics/security-modeling/v3/securities/upsert | Create or update securities


# **delete_securities**
> SMDeleteResponseRoot delete_securities()

Delete existing securities

This endpoint deletes existing securities.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import security_modeling_api
from fds.analyticsapi.engines.model.sm_delete_response_root import SMDeleteResponseRoot
from fds.analyticsapi.engines.model.sm_delete_parameters_root import SMDeleteParametersRoot
from pprint import pprint
# Defining the host is optional and defaults to https://api.factset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fds.analyticsapi.engines.Configuration(
    host = "https://api.factset.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = fds.analyticsapi.engines.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization: Bearer
configuration = fds.analyticsapi.engines.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with fds.analyticsapi.engines.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_modeling_api.SecurityModelingApi(api_client)
    sm_delete_parameters_root = SMDeleteParametersRoot(
        data=[
            SMDeleteParameters(
                security_name="security_name_example",
                location="location_example",
                asofdate="asofdate_example",
                security_type="Bond",
            ),
        ],
        meta=None,
    ) # SMDeleteParametersRoot |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete existing securities
        api_response = api_instance.delete_securities(sm_delete_parameters_root=sm_delete_parameters_root)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling SecurityModelingApi->delete_securities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sm_delete_parameters_root** | [**SMDeleteParametersRoot**](SMDeleteParametersRoot.md)|  | [optional]

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: [**SMDeleteResponseRoot**](SMDeleteResponseRoot.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, deletes existing securities. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header. Header needs to be set to application/json. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_securities**
> SMRetrieveResponseRoot get_securities()

Get existing securities

This endpoint gets all existing securities.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import security_modeling_api
from fds.analyticsapi.engines.model.sm_retrieve_parameters_root import SMRetrieveParametersRoot
from fds.analyticsapi.engines.model.sm_retrieve_response_root import SMRetrieveResponseRoot
from pprint import pprint
# Defining the host is optional and defaults to https://api.factset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fds.analyticsapi.engines.Configuration(
    host = "https://api.factset.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = fds.analyticsapi.engines.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization: Bearer
configuration = fds.analyticsapi.engines.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with fds.analyticsapi.engines.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_modeling_api.SecurityModelingApi(api_client)
    sm_retrieve_parameters_root = SMRetrieveParametersRoot(
        data=[
            SMRetrieveParameters(
                security_name="security_name_example",
                location="location_example",
                asofdate="asofdate_example",
                security_type="Bond",
            ),
        ],
        meta=None,
    ) # SMRetrieveParametersRoot |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get existing securities
        api_response = api_instance.get_securities(sm_retrieve_parameters_root=sm_retrieve_parameters_root)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling SecurityModelingApi->get_securities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sm_retrieve_parameters_root** | [**SMRetrieveParametersRoot**](SMRetrieveParametersRoot.md)|  | [optional]

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: [**SMRetrieveResponseRoot**](SMRetrieveResponseRoot.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, returns a list of existing securities. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header. Header needs to be set to application/json. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_fields**
> SMTemplateFieldPropertiesRoot get_template_fields(template)

Get template fields

This endpoint gets template fields.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import security_modeling_api
from fds.analyticsapi.engines.model.sm_template_field_properties_root import SMTemplateFieldPropertiesRoot
from fds.analyticsapi.engines.model.client_error_response import ClientErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.factset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fds.analyticsapi.engines.Configuration(
    host = "https://api.factset.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = fds.analyticsapi.engines.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization: Bearer
configuration = fds.analyticsapi.engines.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with fds.analyticsapi.engines.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_modeling_api.SecurityModelingApi(api_client)
    template = "template_example" # str | Template name

    # example passing only required values which don't have defaults set
    try:
        # Get template fields
        api_response = api_instance.get_template_fields(template)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling SecurityModelingApi->get_template_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **str**| Template name |

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: [**SMTemplateFieldPropertiesRoot**](SMTemplateFieldPropertiesRoot.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, returns a list of all template fields. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid template. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | Template not found. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header. Header needs to be set to application/json. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_securities**
> SMCreateResponseRoot upsert_securities()

Create or update securities

This endpoint is to create or update existing securities.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import security_modeling_api
from fds.analyticsapi.engines.model.sm_create_parameters_root import SMCreateParametersRoot
from fds.analyticsapi.engines.model.sm_create_response_root import SMCreateResponseRoot
from pprint import pprint
# Defining the host is optional and defaults to https://api.factset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fds.analyticsapi.engines.Configuration(
    host = "https://api.factset.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = fds.analyticsapi.engines.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization: Bearer
configuration = fds.analyticsapi.engines.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with fds.analyticsapi.engines.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_modeling_api.SecurityModelingApi(api_client)
    sm_create_parameters_root = SMCreateParametersRoot(
        data=[
            SMCreateParameters(
                security_name="security_name_example",
                location="location_example",
                asofdate="asofdate_example",
                fields=
                    _144a_flag=True,
                    aperiodic_multipliers=[
                        3.14,
                    ],
                    aperiodic_reset_dates=[
                        "aperiodic_reset_dates_example",
                    ],
                    aperiodic_spreads=[],
                    business_day_conv="business_day_conv_example",
                    call_announced_date="call_announced_date_example",
                    call_dates=[],
                    call_freq="call_freq_example",
                    call_notice_days=1,
                    call_prices=[],
                    cash_rate=3.14,
                    cognity="cognity_example",
                    conversion_identifier="conversion_identifier_example",
                    conversion_ratio=3.14,
                    conversion_type="conversion_type_example",
                    convertible_flag=True,
                    country="country_example",
                    coupon=3.14,
                    coupon_type="coupon_type_example",
                    credit_spread_adjustment_single=3.14,
                    currency="currency_example",
                    day_count_basis="day_count_basis_example",
                    defaulted_date="defaulted_date_example",
                    federal_tax_exempt_flag=True,
                    first_pay_date="first_pay_date_example",
                    first_reset_date="first_reset_date_example",
                    float_formula="float_formula_example",
                    flt_day_count_basis="flt_day_count_basis_example",
                    flt_first_pay_date="flt_first_pay_date_example",
                    flt_pay_freq="flt_pay_freq_example",
                    hist_coupon_dates=[],
                    hist_coupons=[],
                    hist_rcv_assump_dates=[],
                    hist_rcv_assump_months=[
                        1,
                    ],
                    hist_rcv_assump_rates=[],
                    hist_rcv_assump_target_dates=[],
                    inflation_type="inflation_type_example",
                    issue_date="issue_date_example",
                    issue_name="issue_name_example",
                    issuer_id="issuer_id_example",
                    last_modified_source="last_modified_source_example",
                    last_modified_source_meta="last_modified_source_meta_example",
                    last_modified_time="last_modified_time_example",
                    life_cap=3.14,
                    life_floor=3.14,
                    lockout_days=1,
                    look_back_days=1,
                    make_whole_call_flag=True,
                    make_whole_expire_date="make_whole_expire_date_example",
                    make_whole_spread=3.14,
                    matrix_dates=[],
                    matrix_multipliers=[],
                    matrix_priced_flag=True,
                    matrix_spreads=[],
                    matrix_use_schedule_flag=True,
                    maturity_date="maturity_date_example",
                    maturity_price=3.14,
                    months_to_recovery=3.14,
                    multiplier=3.14,
                    notional_flag=True,
                    observation_shift=1,
                    orig_amt_issued=3.14,
                    parent_name="parent_name_example",
                    par_price=3.14,
                    parser_info="parser_info_example",
                    payment_delay=1,
                    pay_freq="pay_freq_example",
                    period_cap=3.14,
                    period_floor=3.14,
                    pik_exp_date="pik_exp_date_example",
                    pik_rate=1,
                    preferred_sec_ex_date_len=1,
                    preferred_sec_ex_date_units="preferred_sec_ex_date_units_example",
                    preferred_sec_flag=True,
                    preferred_sec_type="preferred_sec_type_example",
                    principal_type="principal_type_example",
                    put_dates=[],
                    put_notice_days=1,
                    put_freq="put_freq_example",
                    put_prices=[],
                    pvt_placement_flag=True,
                    rating_fitch="rating_fitch_example",
                    rating_fitch_dates=[],
                    rating_fitch_values=[],
                    rating_moodys_dates=[],
                    rating_moodys_values=[],
                    rating_sp_dates=[],
                    rating_sp_values=[],
                    recovery_percentage=3.14,
                    redemption_date="redemption_date_example",
                    redemption_opt="redemption_opt_example",
                    redemption_price=3.14,
                    reinstated_date="reinstated_date_example",
                    reset_delay=1,
                    reset_freq="reset_freq_example",
                    ref_index="ref_index_example",
                    secondary_to_vendor_flag=True,
                    sector="sector_example",
                    sector_barclay1="sector_barclay1_example",
                    sector_barclay2="sector_barclay2_example",
                    sector_barclay3="sector_barclay3_example",
                    sector_barclay4="sector_barclay4_example",
                    sector_def="sector_def_example",
                    sector_industry="sector_industry_example",
                    sector_main="sector_main_example",
                    sector_merrill1="sector_merrill1_example",
                    sector_merrill2="sector_merrill2_example",
                    sector_merrill3="sector_merrill3_example",
                    sector_merrill4="sector_merrill4_example",
                    sector_sub_group="sector_sub_group_example",
                    sink_amts=[],
                    sink_dates=[],
                    spread=3.14,
                    state="state_example",
                    status="status_example",
                    status_dates=[],
                    status_values=[],
                    step_cash_rates=[],
                    step_coupon_dates=[],
                    step_coupons=[],
                    step_pik_rates=[],
                    vendor_coverage_date="vendor_coverage_date_example",
                    v_rdn_flag=True,
                ,
            ),
        ],
        meta=None,
    ) # SMCreateParametersRoot |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update securities
        api_response = api_instance.upsert_securities(sm_create_parameters_root=sm_create_parameters_root)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling SecurityModelingApi->upsert_securities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sm_create_parameters_root** | [**SMCreateParametersRoot**](SMCreateParametersRoot.md)|  | [optional]

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: [**SMCreateResponseRoot**](SMCreateResponseRoot.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, returns a status of operation along with errors and warnings if found any. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header. Header needs to be set to application/json. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

