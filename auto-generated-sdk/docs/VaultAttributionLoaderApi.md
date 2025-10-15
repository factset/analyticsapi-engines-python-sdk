
# fds.analyticsapi.engines.VaultAttributionLoaderApi

All URIs are relative to *https://api.factset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vault_attribution_loader**](VaultAttributionLoaderApi.md#vault_attribution_loader) | **POST** /analytics/engines/vault/v3/load/{batchId} | Vault - External Attribution Loader


# **vault_attribution_loader**
> VaultAttributionLoaderResponseRoot vault_attribution_loader(batch_id)

Vault - External Attribution Loader

This endpoint loads Vault External Attributions.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import vault_attribution_loader_api
from fds.analyticsapi.engines.model.vault_attribution_loader_response_root import VaultAttributionLoaderResponseRoot
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
    api_instance = vault_attribution_loader_api.VaultAttributionLoaderApi(api_client)
    batch_id = "batchId_example" # str | 
    file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Vault - External Attribution Loader
        api_response = api_instance.vault_attribution_loader(batch_id)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling VaultAttributionLoaderApi->vault_attribution_loader: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Vault - External Attribution Loader
        api_response = api_instance.vault_attribution_loader(batch_id, file=file)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling VaultAttributionLoaderApi->vault_attribution_loader: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**|  |
 **file** | **file_type, none_type**|  | [optional]

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: [**VaultAttributionLoaderResponseRoot**](VaultAttributionLoaderResponseRoot.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, returns a status of operation along with errors and warnings if found any. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Bad Request |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header. Header needs to be set to application/json. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

