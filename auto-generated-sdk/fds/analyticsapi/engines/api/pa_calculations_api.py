"""
    Engines API

    Allow clients to fetch Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: 2
    Contact: analytics.api.support@factset.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from fds.analyticsapi.engines.api_client import ApiClient, Endpoint as _Endpoint
from fds.analyticsapi.engines.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from fds.analyticsapi.engines.model.pa_calculation_parameters import PACalculationParameters


class PACalculationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __cancel_pa_calculation_by_id(
            self,
            id,
            **kwargs
        ):
            """Cancel PA calculation by id  # noqa: E501

            This is the endpoint to cancel a previously submitted calculation.  Instead of doing a GET on the polling URL, cancel the request by doing a DELETE.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.cancel_pa_calculation_by_id(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): from url, provided from the location header in the Run Calculation endpoint

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.cancel_pa_calculation_by_id = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/analytics/engines/pa/v2/calculations/{id}',
                'operation_id': 'cancel_pa_calculation_by_id',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__cancel_pa_calculation_by_id
        )

        def __get_pa_calculation_by_id(
            self,
            id,
            **kwargs
        ):
            """Get PA calculation by id  # noqa: E501

            This is the endpoint to check on the progress of a previously requested calculation.  If the calculation has finished computing, the body of the response will contain the requested document in JSON.  Otherwise, the calculation is still running and the X-FactSet-Api-PickUp-Progress header will contain a progress percentage.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_pa_calculation_by_id(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): from url, provided from the location header in the Run Calculation endpoint

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.get_pa_calculation_by_id = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/analytics/engines/pa/v2/calculations/{id}',
                'operation_id': 'get_pa_calculation_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_pa_calculation_by_id
        )

        def __run_pa_calculation(
            self,
            **kwargs
        ):
            """Run PA Calculation  # noqa: E501

            This endpoint runs the PA calculation specified in the POST body parameters.  It must be used first before polling or cancelling endpoints.  A successful response will contain the URL to poll for the result of the calculation.    Remarks:    * Any settings in POST body will act as a one-time override over the settings saved in the PA template.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.run_pa_calculation(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                pa_calculation_parameters (PACalculationParameters): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.run_pa_calculation = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/analytics/engines/pa/v2/calculations',
                'operation_id': 'run_pa_calculation',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'pa_calculation_parameters',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pa_calculation_parameters':
                        (PACalculationParameters,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'pa_calculation_parameters': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__run_pa_calculation
        )
