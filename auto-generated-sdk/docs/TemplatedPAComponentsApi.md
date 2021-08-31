
# fds.analyticsapi.engines.TemplatedPAComponentsApi

All URIs are relative to *https://api.factset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_templated_pa_components**](TemplatedPAComponentsApi.md#create_templated_pa_components) | **POST** /analytics/engines/pa/v3/templated-components | Create templated PA component
[**delete_templated_pa_components**](TemplatedPAComponentsApi.md#delete_templated_pa_components) | **DELETE** /analytics/engines/pa/v3/templated-components/{id} | Delete templated PA component
[**update_templated_pa_components**](TemplatedPAComponentsApi.md#update_templated_pa_components) | **PUT** /analytics/engines/pa/v3/templated-components/{id} | Update templated PA component


# **create_templated_pa_components**
> TemplatedPAComponentSummaryRoot create_templated_pa_components(templated_pa_component_parameters_root)

Create templated PA component

This endpoint creates new component based off of linked PA template or unlinked PA template.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import templated_pa_components_api
from fds.analyticsapi.engines.model.templated_pa_component_summary_root import TemplatedPAComponentSummaryRoot
from fds.analyticsapi.engines.model.templated_pa_component_parameters_root import TemplatedPAComponentParametersRoot
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
    api_instance = templated_pa_components_api.TemplatedPAComponentsApi(api_client)
    templated_pa_component_parameters_root = TemplatedPAComponentParametersRoot(
        data=TemplatedPAComponentParameters(
            directory="directory_example",
            parent_template_id="parent_template_id_example",
            description="description_example",
            component_data=PAComponentData(
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
                groups=[
                    PACalculationGroup(
                        id="id_example",
                    ),
                ],
                columns=[
                    PACalculationColumn(
                        id="id_example",
                        statistics=[
                            "statistics_example",
                        ],
                    ),
                ],
                dates=PADateParameters(
                    startdate="startdate_example",
                    enddate="enddate_example",
                    frequency="frequency_example",
                ),
                currencyisocode="currencyisocode_example",
                componentdetail="componentdetail_example",
            ),
        ),
        meta={},
    ) # TemplatedPAComponentParametersRoot | Request Parameters

    # example passing only required values which don't have defaults set
    try:
        # Create templated PA component
        api_response = api_instance.create_templated_pa_components(templated_pa_component_parameters_root)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling TemplatedPAComponentsApi->create_templated_pa_components: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templated_pa_component_parameters_root** | [**TemplatedPAComponentParametersRoot**](TemplatedPAComponentParametersRoot.md)| Request Parameters |

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: [**TemplatedPAComponentSummaryRoot**](TemplatedPAComponentSummaryRoot.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Expected response, templated PA component created successfully. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid data provided. Please check the request parameters before attempting again. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | Template not found. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header. Header needs to be set to application/json. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_templated_pa_components**
> delete_templated_pa_components(id)

Delete templated PA component

This endpoint deletes an existing templated PA component

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import templated_pa_components_api
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
    api_instance = templated_pa_components_api.TemplatedPAComponentsApi(api_client)
    id = "id_example" # str | Unique identifier for a templated PA component

    # example passing only required values which don't have defaults set
    try:
        # Delete templated PA component
        api_instance.delete_templated_pa_components(id)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling TemplatedPAComponentsApi->delete_templated_pa_components: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for a templated PA component |

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
**204** | Expected response, deleted the templated PA component successfully. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid data provided. Please check the request parameters before attempting again. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | Component not found. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header. Header needs to be set to application/json. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_templated_pa_components**
> TemplatedPAComponentSummaryRoot update_templated_pa_components(id, templated_pa_component_update_parameters_root)

Update templated PA component

This endpoint allows the user to change the request body from an existing templated PA component.

### Example

* Basic Authentication (Basic):
* Bearer Authentication (Bearer):
```python
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.api import templated_pa_components_api
from fds.analyticsapi.engines.model.templated_pa_component_summary_root import TemplatedPAComponentSummaryRoot
from fds.analyticsapi.engines.model.client_error_response import ClientErrorResponse
from fds.analyticsapi.engines.model.templated_pa_component_update_parameters_root import TemplatedPAComponentUpdateParametersRoot
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
    api_instance = templated_pa_components_api.TemplatedPAComponentsApi(api_client)
    id = "id_example" # str | Unique identifier for a templated PA component
    templated_pa_component_update_parameters_root = TemplatedPAComponentUpdateParametersRoot(
        data=TemplatedPAComponentUpdateParameters(
            parent_template_id="parent_template_id_example",
            description="description_example",
            component_data=PAComponentData(
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
                groups=[
                    PACalculationGroup(
                        id="id_example",
                    ),
                ],
                columns=[
                    PACalculationColumn(
                        id="id_example",
                        statistics=[
                            "statistics_example",
                        ],
                    ),
                ],
                dates=PADateParameters(
                    startdate="startdate_example",
                    enddate="enddate_example",
                    frequency="frequency_example",
                ),
                currencyisocode="currencyisocode_example",
                componentdetail="componentdetail_example",
            ),
        ),
        meta={},
    ) # TemplatedPAComponentUpdateParametersRoot | Request Parameters

    # example passing only required values which don't have defaults set
    try:
        # Update templated PA component
        api_response = api_instance.update_templated_pa_components(id, templated_pa_component_update_parameters_root)
        pprint(api_response)
    except fds.analyticsapi.engines.ApiException as e:
        print("Exception when calling TemplatedPAComponentsApi->update_templated_pa_components: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for a templated PA component |
 **templated_pa_component_update_parameters_root** | [**TemplatedPAComponentUpdateParametersRoot**](TemplatedPAComponentUpdateParametersRoot.md)| Request Parameters |

### Return type

 - A tuple with response data, HTTP status code and response headers.
 - **Response datatype**: [**TemplatedPAComponentSummaryRoot**](TemplatedPAComponentSummaryRoot.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, updated successfully. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**400** | Invalid data provided. Please check the request parameters before attempting again. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**404** | Component or template not found. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**401** | Missing or invalid authentication. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**403** | User is forbidden with current credentials |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**406** | Unsupported Accept header. Header needs to be set to application/json. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-FactSet-Api-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-FactSet-Api-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  |
**429** | Rate limit reached. Wait till the time specified in Retry-After header value to make further requests. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * Retry-After - Time to wait in seconds before making a new request as the rate limit has reached. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

