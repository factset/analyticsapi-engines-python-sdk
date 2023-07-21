
# fds.analyticsapi.engines.PACalculationsApi

All URIs are relative to *https://api.factset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_calculation_by_id**](PACalculationsApi.md#cancel_calculation_by_id) | **DELETE** /analytics/engines/pa/v3/calculations/{id} | Cancel PA calculation by id
[**get_all_calculations**](PACalculationsApi.md#get_all_calculations) | **GET** /analytics/engines/pa/v3/calculations | Get all calculations
[**get_calculation_parameters**](PACalculationsApi.md#get_calculation_parameters) | **GET** /analytics/engines/pa/v3/calculations/{id} | Get PA calculation parameters by id
[**get_calculation_status_by_id**](PACalculationsApi.md#get_calculation_status_by_id) | **GET** /analytics/engines/pa/v3/calculations/{id}/status | Get PA calculation status by id
[**get_calculation_unit_result_by_id**](PACalculationsApi.md#get_calculation_unit_result_by_id) | **GET** /analytics/engines/pa/v3/calculations/{id}/units/{unitId}/result | Get PA calculation result by id
[**post_and_calculate**](PACalculationsApi.md#post_and_calculate) | **POST** /analytics/engines/pa/v3/calculations | Create and Run PA calculation
[**put_and_calculate**](PACalculationsApi.md#put_and_calculate) | **PUT** /analytics/engines/pa/v3/calculations/{id} | Create or Update PA calculation and run it.


# **cancel_calculation_by_id**
> cancel_calculation_by_id(id)

Cancel PA calculation by id

This is the endpoint to cancel a previously submitted calculation.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import pa_calculations_api
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
    api_instance = pa_calculations_api.PACalculationsApi(api_client)
    id = "id_example" # str | from url, provided from the location header in the Create and Run PA calculation endpoint

    # example passing only required values which don't have defaults set
    try:
        # Cancel PA calculation by id
        api_instance.cancel_calculation_by_id(id)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling PACalculationsApi->cancel_calculation_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| from url, provided from the location header in the Create and Run PA calculation endpoint |

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: None (empty response body)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Expected response, calculation was canceled successfully. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid identifier provided. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | There was no request for the calculation identifier provided, or the request was already canceled for the provided identifier. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_calculations**
> CalculationsSummaryRoot get_all_calculations()

Get all calculations

This endpoints returns all calculation requests.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import pa_calculations_api
from fds.analyticsapi.engines.model.calculations_summary_root import CalculationsSummaryRoot
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
    api_instance = pa_calculations_api.PACalculationsApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get all calculations
        api_response = api_instance.get_all_calculations()
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling PACalculationsApi->get_all_calculations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | defaults to 1

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: [**CalculationsSummaryRoot**](CalculationsSummaryRoot.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of calculation requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid page number. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | No calculation found. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header. Header needs to be set to application/json. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calculation_parameters**
> PACalculationParametersRoot get_calculation_parameters(id)

Get PA calculation parameters by id

This is the endpoint that returns the calculation parameters passed for a calculation.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import pa_calculations_api
from fds.analyticsapi.engines.model.pa_calculation_parameters_root import PACalculationParametersRoot
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
    api_instance = pa_calculations_api.PACalculationsApi(api_client)
    id = "id_example" # str | from url, provided from the location header in the Create and Run PA calculation endpoint

    # example passing only required values which don't have defaults set
    try:
        # Get PA calculation parameters by id
        api_response = api_instance.get_calculation_parameters(id)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling PACalculationsApi->get_calculation_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| from url, provided from the location header in the Create and Run PA calculation endpoint |

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: [**PACalculationParametersRoot**](PACalculationParametersRoot.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, returns the PA calculation parameters. |  * Content-Encoding - Standard HTTP header. Header value based on Accept-Encoding Request header. <br>  * Content-Type - Standard HTTP header. <br>  * Transfer-Encoding - Standard HTTP header. Header value will be set to Chunked if Accept-Encoding header is specified. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid identifier provided. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | Calculation id not found |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calculation_status_by_id**
> CalculationStatusRoot get_calculation_status_by_id(id)

Get PA calculation status by id

This is the endpoint to check on the progress of a previously requested calculation.  If the calculation has finished computing, the location header will point to the result url.  Otherwise, the calculation is still running and the X-FactSet-Api-PickUp-Progress header will contain a progress percentage.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import pa_calculations_api
from fds.analyticsapi.engines.model.calculation_status_root import CalculationStatusRoot
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
    api_instance = pa_calculations_api.PACalculationsApi(api_client)
    id = "id_example" # str | from url, provided from the location header in the Create and Run PA calculation endpoint

    # example passing only required values which don't have defaults set
    try:
        # Get PA calculation status by id
        api_response = api_instance.get_calculation_status_by_id(id)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling PACalculationsApi->get_calculation_status_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| from url, provided from the location header in the Create and Run PA calculation endpoint |

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: [**CalculationStatusRoot**](CalculationStatusRoot.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response once calculation is completed. |  * Content-Encoding - Standard HTTP header. Header value based on Accept-Encoding Request header. <br>  * Content-Type - Standard HTTP header. <br>  * Transfer-Encoding - Standard HTTP header. Header value will be set to Chunked if Accept-Encoding header is specified. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**202** | Expected response returned if the calculation is not yet completed, should contain X-FactSet-Api-PickUp-Progress header. |  * X-FactSet-Api-PickUp-Progress - FactSet&#39;s progress header. <br>  * Cache-Control - Standard HTTP header. Header will specify max-age in seconds. Polling can be adjusted based on the max-age value. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid identifier provided. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | Calculation was already returned, provided id was not a requested calculation, or the calculation was cancelled |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calculation_unit_result_by_id**
> ObjectRoot get_calculation_unit_result_by_id(id, unit_id)

Get PA calculation result by id

This is the endpoint to get the result of a previously requested calculation.  If the calculation has finished computing, the body of the response will contain the requested document in JSON.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import pa_calculations_api
from fds.analyticsapi.engines.model.object_root import ObjectRoot
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
    api_instance = pa_calculations_api.PACalculationsApi(api_client)
    id = "id_example" # str | from url, provided from the location header in the Get PA calculation status by id endpoint
    unit_id = "unitId_example" # str | from url, provided from the location header in the Get PA calculation status by id endpoint

    # example passing only required values which don't have defaults set
    try:
        # Get PA calculation result by id
        api_response = api_instance.get_calculation_unit_result_by_id(id, unit_id)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling PACalculationsApi->get_calculation_unit_result_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| from url, provided from the location header in the Get PA calculation status by id endpoint |
 **unit_id** | **str**| from url, provided from the location header in the Get PA calculation status by id endpoint |

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: [**ObjectRoot**](ObjectRoot.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-protobuf


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response once calculation is completed, returns JSON in the format specified in the Calculation parameters. |  * Content-Encoding - Standard HTTP header. Header value based on Accept-Encoding Request header. <br>  * Content-Type - Standard HTTP header. <br>  * Transfer-Encoding - Standard HTTP header. Header value will be set to Chunked if Accept-Encoding header is specified. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid identifier provided. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | Calculation was already returned, provided id was not a requested calculation, or the calculation was cancelled |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_and_calculate**
> CalculationStatusRoot post_and_calculate()

Create and Run PA calculation

This endpoint runs the PA calculation specified in the POST body parameters.  It can take one or more calculation units as input.    Remarks:    * Any settings in POST body will act as a one-time override over the settings saved in the PA template.    *   Account identifiers must have .ACCT or .ACTM extension or BENCH: prefix. Holdings mode can be optionally set for every account.       Possible values for holdings mode are B&H (Buy and Hold), TBR (Transaction based returns), OMS (Order Management System),       VLT (Vaulted returns) or EXT (External Returns Data). Default holdings mode value is B&H.     *   If we are overriding the grouping with a frequency, we will be overriding the grouping saved to the original component and also overriding       the default frequency of the Beginning of Period to whatever we pass in the request body.        *   If we are overriding gouping frequency without overriding the group id it will not be applied to the default groupings saved to the original component.    *   Componentdetail supports securities, groups, groupsall, and totals levels of granularity. However, if no value is passed, the default value is 'securities'.      Additionally, while 'groupsall' returns all the group levels in the PA component,      setting componentdetail to 'groups' only returns the expanded or collapsed group levels within the PA component.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import pa_calculations_api
from fds.analyticsapi.engines.model.calculation_status_root import CalculationStatusRoot
from fds.analyticsapi.engines.model.object_root import ObjectRoot
from fds.analyticsapi.engines.model.pa_calculation_parameters_root import PACalculationParametersRoot
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
    api_instance = pa_calculations_api.PACalculationsApi(api_client)
    x_fact_set_api_long_running_deadline = 1 # int | Long running deadline in seconds when only one unit is passed in the POST body. (optional)
    cache_control = "Cache-Control_example" # str | Standard HTTP header.  Accepts max-stale. (optional)
    pa_calculation_parameters_root = PACalculationParametersRoot(
        data={
            "key": PACalculationParameters(
                componentid="componentid_example",
                accounts=[
                    PAIdentifier(
                        id="id_example",
                        holdingsmode="holdingsmode_example",
                    ),
                ],
                benchmarks=[
                    PAIdentifier(
                        id="id_example",
                        holdingsmode="holdingsmode_example",
                    ),
                ],
                dates=PADateParameters(
                    startdate="startdate_example",
                    enddate="enddate_example",
                    frequency="frequency_example",
                ),
                groups=[
                    PACalculationGroup(
                        id="id_example",
                        frequency="frequency_example",
                    ),
                ],
                currencyisocode="currencyisocode_example",
                columns=[
                    PACalculationColumn(
                        id="id_example",
                        statistics=[
                            "statistics_example",
                        ],
                    ),
                ],
                datasources=PACalculationDataSources(
                    portfoliopricingsources=[
                        PACalculationPricingSource(
                            id="id_example",
                        ),
                    ],
                    benchmarkpricingsources=[
                        PACalculationPricingSource(
                            id="id_example",
                        ),
                    ],
                    useportfoliopricingsourcesforbenchmark=True,
                ),
                componentdetail="componentdetail_example",
            ),
        },
        meta=CalculationMeta(
            contentorganization="SimplifiedRow",
            stach_content_organization="SimplifiedRow",
            contenttype="Json",
            format="JsonStach",
        ),
    ) # PACalculationParametersRoot | Calculation Parameters (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create and Run PA calculation
        api_response = api_instance.post_and_calculate(x_fact_set_api_long_running_deadline=x_fact_set_api_long_running_deadline, cache_control=cache_control, pa_calculation_parameters_root=pa_calculation_parameters_root)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling PACalculationsApi->post_and_calculate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fact_set_api_long_running_deadline** | **int**| Long running deadline in seconds when only one unit is passed in the POST body. | [optional]
 **cache_control** | **str**| Standard HTTP header.  Accepts max-stale. | [optional]
 **pa_calculation_parameters_root** | [**PACalculationParametersRoot**](PACalculationParametersRoot.md)| Calculation Parameters | [optional]

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: (For 202 status - [**CalculationStatusRoot**](CalculationStatusRoot.md))(For 201 status - [**ObjectRoot**](ObjectRoot.md))(For 200 status - [**CalculationStatusRoot**](CalculationStatusRoot.md))

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/x-protobuf


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Expected response, contains the poll URL in the Location header. |  * Location - URL to poll for the resulting calculation <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**201** | Expected response if the calculation has one unit and is completed in a short span, returns JSON in the format specified in the Calculation parameters. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**200** | Expected response, if the calculation has one unit and is completed with an error. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid calculation parameters. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | One or more calculation settings were unavailable. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**415** | Missing/Invalid Content-Type header. Header needs to be set to application/json. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Cancel older requests using Cancel Calculation endpoint or wait for older requests to finish/expire. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_and_calculate**
> CalculationStatusRoot put_and_calculate(id)

Create or Update PA calculation and run it.

This endpoint updates and run the PA calculation specified in the PUT body parameters. This also allows creating new PA calculations with custom ids.  It can take one or more calculation units as input.    Remarks:    * Any settings in PUT body will act as a one-time override over the settings saved in the PA template.    *   Account identifiers must have .ACCT or .ACTM extension or BENCH: prefix. Holdings mode can be optionally set for every account.       Possible values for holdings mode are B&H (Buy and Hold), TBR (Transaction based returns), OMS (Order Management System),       VLT (Vaulted returns) or EXT (External Returns Data). Default holdings mode value is B&H.    *   If we are overriding the grouping with a frequency, we will be overriding the grouping saved to the original component and also overriding       the default frequency of the Beginning of Period to whatever we pass in the request body.        *   If we are overriding gouping frequency without overriding the group id it will not be applied to the default groupings saved to the original component.    *   Componentdetail supports securities, groups, groupsall, and totals levels of granularity. However, if no value is passed, the default value is 'securities'.      Additionally, while 'groupsall' returns all the group levels in the PA component,      setting componentdetail to 'groups' only returns the expanded or collapsed group levels within the PA component.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import pa_calculations_api
from fds.analyticsapi.engines.model.calculation_status_root import CalculationStatusRoot
from fds.analyticsapi.engines.model.object_root import ObjectRoot
from fds.analyticsapi.engines.model.pa_calculation_parameters_root import PACalculationParametersRoot
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
    api_instance = pa_calculations_api.PACalculationsApi(api_client)
    id = "id_example" # str | from url, provided from the location header in the Create and Run PA calculation endpoint
    x_fact_set_api_long_running_deadline = 1 # int | Long running deadline in seconds when only one unit is passed in the PUT body. (optional)
    cache_control = "Cache-Control_example" # str | Standard HTTP header.  Accepts max-stale. (optional)
    pa_calculation_parameters_root = PACalculationParametersRoot(
        data={
            "key": PACalculationParameters(
                componentid="componentid_example",
                accounts=[
                    PAIdentifier(
                        id="id_example",
                        holdingsmode="holdingsmode_example",
                    ),
                ],
                benchmarks=[
                    PAIdentifier(
                        id="id_example",
                        holdingsmode="holdingsmode_example",
                    ),
                ],
                dates=PADateParameters(
                    startdate="startdate_example",
                    enddate="enddate_example",
                    frequency="frequency_example",
                ),
                groups=[
                    PACalculationGroup(
                        id="id_example",
                        frequency="frequency_example",
                    ),
                ],
                currencyisocode="currencyisocode_example",
                columns=[
                    PACalculationColumn(
                        id="id_example",
                        statistics=[
                            "statistics_example",
                        ],
                    ),
                ],
                datasources=PACalculationDataSources(
                    portfoliopricingsources=[
                        PACalculationPricingSource(
                            id="id_example",
                        ),
                    ],
                    benchmarkpricingsources=[
                        PACalculationPricingSource(
                            id="id_example",
                        ),
                    ],
                    useportfoliopricingsourcesforbenchmark=True,
                ),
                componentdetail="componentdetail_example",
            ),
        },
        meta=CalculationMeta(
            contentorganization="SimplifiedRow",
            stach_content_organization="SimplifiedRow",
            contenttype="Json",
            format="JsonStach",
        ),
    ) # PACalculationParametersRoot | Calculation Parameters (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or Update PA calculation and run it.
        api_response = api_instance.put_and_calculate(id)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling PACalculationsApi->put_and_calculate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or Update PA calculation and run it.
        api_response = api_instance.put_and_calculate(id, x_fact_set_api_long_running_deadline=x_fact_set_api_long_running_deadline, cache_control=cache_control, pa_calculation_parameters_root=pa_calculation_parameters_root)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling PACalculationsApi->put_and_calculate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| from url, provided from the location header in the Create and Run PA calculation endpoint |
 **x_fact_set_api_long_running_deadline** | **int**| Long running deadline in seconds when only one unit is passed in the PUT body. | [optional]
 **cache_control** | **str**| Standard HTTP header.  Accepts max-stale. | [optional]
 **pa_calculation_parameters_root** | [**PACalculationParametersRoot**](PACalculationParametersRoot.md)| Calculation Parameters | [optional]

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: (For 202 status - [**CalculationStatusRoot**](CalculationStatusRoot.md))(For 200 status - [**CalculationStatusRoot**](CalculationStatusRoot.md))(For 201 status - [**ObjectRoot**](ObjectRoot.md))

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/x-protobuf


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Expected response, contains the poll URL in the Location header. |  * Location - URL to poll for the resulting calculation <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**200** | Expected response, if the calculation has one unit and is completed with an error. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**201** | Expected response if the calculation has one unit and is completed in a short span, returns JSON in the format specified in the Calculation parameters. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid Calculation Parameters. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | One or more calculation settings were unavailable. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**409** | Duplicate calculation exists with same parameters. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**415** | Missing/Invalid Content-Type header. Header needs to be set to application/json. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Cancel older requests using Cancel Calculation endpoint or wait for older requests to finish/expire. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

