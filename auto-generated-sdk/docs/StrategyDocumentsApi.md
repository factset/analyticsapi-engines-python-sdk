# fds.analyticsapi.engines.StrategyDocumentsApi

All URIs are relative to *https://api.factset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_axioma_equity_strategy_documents**](StrategyDocumentsApi.md#get_axioma_equity_strategy_documents) | **GET** /analytics/engines/axp/v1/strategies/{path} | Get Axioma Equity strategy documents and sub-directories in a directory
[**get_axioma_fi_strategy_documents**](StrategyDocumentsApi.md#get_axioma_fi_strategy_documents) | **GET** /analytics/engines/afi/v1/strategies/{path} | Get Axioma FI strategy documents and sub-directories in a directory
[**get_barra_strategy_documents**](StrategyDocumentsApi.md#get_barra_strategy_documents) | **GET** /analytics/engines/bpm/v1/strategies/{path} | Get Barra strategy documents and sub-directories in a directory
[**get_fpo_strategy_documents**](StrategyDocumentsApi.md#get_fpo_strategy_documents) | **GET** /analytics/engines/fpo/v1/strategies/{path} | Get FactSet Portfolio Optimizer strategy documents and sub-directories in a directory
[**get_northfield_strategy_documents**](StrategyDocumentsApi.md#get_northfield_strategy_documents) | **GET** /analytics/engines/npo/v1/strategies/{path} | Get Northfield strategy documents and sub-directories in a directory


# **get_axioma_equity_strategy_documents**
> DocumentDirectories get_axioma_equity_strategy_documents(path)

Get Axioma Equity strategy documents and sub-directories in a directory

This endpoint looks up all Axioma Equity strategy documents and sub-directories in a given directory.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.rest import ApiException
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

# Enter a context with an instance of the API client
with fds.analyticsapi.engines.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds.analyticsapi.engines.StrategyDocumentsApi(api_client)
    path = '' # str | The directory to get the strategy documents and sub-directories in (default to '')

    try:
        # Get Axioma Equity strategy documents and sub-directories in a directory
        api_response = api_instance.get_axioma_equity_strategy_documents(path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StrategyDocumentsApi->get_axioma_equity_strategy_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The directory to get the strategy documents and sub-directories in | [default to &#39;&#39;]

### Return type

[**DocumentDirectories**](DocumentDirectories.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, returns a list of Axioma Equity strategy documents and directories |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid query parameter or value provided |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | Path not found |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header.  Header needs to be set to application/json |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in some time |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_axioma_fi_strategy_documents**
> DocumentDirectories get_axioma_fi_strategy_documents(path)

Get Axioma FI strategy documents and sub-directories in a directory

This endpoint looks up all Axioma FI strategy documents and sub-directories in a given directory.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.rest import ApiException
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

# Enter a context with an instance of the API client
with fds.analyticsapi.engines.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds.analyticsapi.engines.StrategyDocumentsApi(api_client)
    path = '' # str | The directory to get the strategy documents and sub-directories in (default to '')

    try:
        # Get Axioma FI strategy documents and sub-directories in a directory
        api_response = api_instance.get_axioma_fi_strategy_documents(path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StrategyDocumentsApi->get_axioma_fi_strategy_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The directory to get the strategy documents and sub-directories in | [default to &#39;&#39;]

### Return type

[**DocumentDirectories**](DocumentDirectories.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, returns a list of Axioma FI strategy documents and directories |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid query parameter or value provided |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | Path not found |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header.  Header needs to be set to application/json |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in some time |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_barra_strategy_documents**
> DocumentDirectories get_barra_strategy_documents(path)

Get Barra strategy documents and sub-directories in a directory

This endpoint looks up all Barra strategy documents and sub-directories in a given directory.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.rest import ApiException
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

# Enter a context with an instance of the API client
with fds.analyticsapi.engines.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds.analyticsapi.engines.StrategyDocumentsApi(api_client)
    path = '' # str | The directory to get the strategy documents and sub-directories in (default to '')

    try:
        # Get Barra strategy documents and sub-directories in a directory
        api_response = api_instance.get_barra_strategy_documents(path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StrategyDocumentsApi->get_barra_strategy_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The directory to get the strategy documents and sub-directories in | [default to &#39;&#39;]

### Return type

[**DocumentDirectories**](DocumentDirectories.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, returns a list of Barra strategy documents and directories |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid query parameter or value provided |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | Path not found |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header.  Header needs to be set to application/json |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in some time |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fpo_strategy_documents**
> DocumentDirectories get_fpo_strategy_documents(path)

Get FactSet Portfolio Optimizer strategy documents and sub-directories in a directory

This endpoint looks up all FactSet Portfolio Optimizer strategy documents and sub-directories in a given directory.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.rest import ApiException
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

# Enter a context with an instance of the API client
with fds.analyticsapi.engines.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds.analyticsapi.engines.StrategyDocumentsApi(api_client)
    path = '' # str | The directory to get the strategy documents and sub-directories in (default to '')

    try:
        # Get FactSet Portfolio Optimizer strategy documents and sub-directories in a directory
        api_response = api_instance.get_fpo_strategy_documents(path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StrategyDocumentsApi->get_fpo_strategy_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The directory to get the strategy documents and sub-directories in | [default to &#39;&#39;]

### Return type

[**DocumentDirectories**](DocumentDirectories.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, returns a list of FactSet Portfolio Optimizer strategy documents and directories |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid query parameter or value provided |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | Path not found |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header.  Header needs to be set to application/json |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in some time |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_northfield_strategy_documents**
> DocumentDirectories get_northfield_strategy_documents(path)

Get Northfield strategy documents and sub-directories in a directory

This endpoint looks up all Northfield strategy documents and sub-directories in a given directory.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.rest import ApiException
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

# Enter a context with an instance of the API client
with fds.analyticsapi.engines.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds.analyticsapi.engines.StrategyDocumentsApi(api_client)
    path = '' # str | The directory to get the strategy documents and sub-directories in (default to '')

    try:
        # Get Northfield strategy documents and sub-directories in a directory
        api_response = api_instance.get_northfield_strategy_documents(path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StrategyDocumentsApi->get_northfield_strategy_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The directory to get the strategy documents and sub-directories in | [default to &#39;&#39;]

### Return type

[**DocumentDirectories**](DocumentDirectories.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, returns a list of Northfield strategy documents and directories |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid query parameter or value provided |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | Path not found |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header.  Header needs to be set to application/json |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in some time |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

