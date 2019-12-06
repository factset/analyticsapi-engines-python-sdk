# fds.analyticsapi.engines.UtilityApi

All URIs are relative to *https://api.factset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_by_url**](UtilityApi.md#get_by_url) | **GET** {url}} | This method fetches data from any Get endpoint.


# **get_by_url**
> object get_by_url(url)

Get by url

This method fetches data from any GET endpoint.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.rest import ApiException
from pprint import pprint
configuration = fds.analyticsapi.engines.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Defining host is optional and default to https://api.factset.com
configuration.host = "https://api.factset.com"
# Create an instance of the API class
api_instance = fds.analyticsapi.engines.UtilityApi(fds.analyticsapi.engines.ApiClient(configuration))
url = 'url_example' # str | Url of the GET endpoint

try:
    # Get by url
    api_response = api_instance.get_by_url(url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->get_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **object**| Url of the GET endpoint | 

### Return type

**object**

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response once the request is successful. |  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-DataDirect-Request-Key - FactSet's request key header. <br>  |
**400** | Invalid identifier provided. |  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-DataDirect-Request-Key - FactSet's request key header. <br>  |
**401** | Missing or invalid authentication. |  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-DataDirect-Request-Key - FactSet's request key header. <br>  |
**403** | User is forbidden with current credentials |  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-DataDirect-Request-Key - FactSet's request key header. <br>  |
**406** | Unsupported Accept header. Header needs to be set to application/json. |  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-DataDirect-Request-Key - FactSet's request key header. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting. |  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-DataDirect-Request-Key - FactSet's request key header. <br>  |
**503** | Request timed out. Retry the request in sometime. |  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-DataDirect-Request-Key - FactSet's request key header. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

