"""
    Engines API

    Allow clients to fetch Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: v3:[pa,spar,vault,pub,quant,fi,axp,afi,npo,bpm,fpo,others],v1:[fiab]
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
from fds.analyticsapi.engines.model.calculation_status_root import CalculationStatusRoot
from fds.analyticsapi.engines.model.client_error_response import ClientErrorResponse
from fds.analyticsapi.engines.model.object_root import ObjectRoot
from fds.analyticsapi.engines.model.quant_calculation_parameters_root import QuantCalculationParametersRoot


class QuantCalculationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_calculation_parameters(
            self,
            id,
            **kwargs
        ):
            """Get Quant Engine calculation parameters by id  # noqa: E501

            This is the endpoint that returns the calculation parameters passed for a calculation.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_calculation_parameters(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): from url, provided from the location header in the Create and Run Quant Engine calculation endpoint

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
                QuantCalculationParametersRoot
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

        self.get_calculation_parameters = _Endpoint(
            settings={
                'response_type': dict({ 200:(QuantCalculationParametersRoot,),  }),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/analytics/engines/quant/v3/calculations/{id}',
                'operation_id': 'get_calculation_parameters',
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
            callable=__get_calculation_parameters
        )

        def __get_calculation_status_by_id(
            self,
            id,
            **kwargs
        ):
            """Get Quant Engine calculation status by id  # noqa: E501

            This is the endpoint to check on the progress of a previously requested calculation.  If the calculation has finished computing, the location header will point to the result url.  Otherwise, the calculation is still running and the X-FactSet-Api-PickUp-Progress header will contain a progress percentage.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_calculation_status_by_id(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): from url, provided from the location header in the Create and Run Quant Engine calculation endpoint

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
                CalculationStatusRoot
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

        self.get_calculation_status_by_id = _Endpoint(
            settings={
                'response_type': dict({ 200:(CalculationStatusRoot,), 202:(CalculationStatusRoot,),  }),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/analytics/engines/quant/v3/calculations/{id}/status',
                'operation_id': 'get_calculation_status_by_id',
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
            callable=__get_calculation_status_by_id
        )

        def __get_calculation_unit_info_by_id(
            self,
            id,
            unit_id,
            **kwargs
        ):
            """Get Quant Engine calculation metadata information by id  # noqa: E501

            This is the endpoint to get the metadata information of a previously requested calculation.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_calculation_unit_info_by_id(id, unit_id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): from url, provided from the location header in the Get Quant calculation status by id endpoint
                unit_id (str): from url, provided from the location header in the Get Quant calculation status by id endpoint

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
                ObjectRoot
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
            kwargs['unit_id'] = \
                unit_id
            return self.call_with_http_info(**kwargs)

        self.get_calculation_unit_info_by_id = _Endpoint(
            settings={
                'response_type': dict({ 200:(ObjectRoot,),  }),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/analytics/engines/quant/v3/calculations/{id}/units/{unitId}/info',
                'operation_id': 'get_calculation_unit_info_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'unit_id',
                ],
                'required': [
                    'id',
                    'unit_id',
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
                    'unit_id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'unit_id': 'unitId',
                },
                'location_map': {
                    'id': 'path',
                    'unit_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/x-protobuf'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_calculation_unit_info_by_id
        )

        def __get_calculation_unit_result_by_id(
            self,
            id,
            unit_id,
            **kwargs
        ):
            """Get Quant Engine calculation result by id  # noqa: E501

            This is the endpoint to get the result of a previously requested calculation.  If the calculation has finished computing, the body of the response will contain the requested document in JSON.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_calculation_unit_result_by_id(id, unit_id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): from url, provided from the location header in the Get Quant Engine calculation status by id endpoint
                unit_id (str): from url, provided from the location header in the Get Quant Engine calculation status by id endpoint

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
                ObjectRoot
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
            kwargs['unit_id'] = \
                unit_id
            return self.call_with_http_info(**kwargs)

        self.get_calculation_unit_result_by_id = _Endpoint(
            settings={
                'response_type': dict({ 200:(ObjectRoot,),  }),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/analytics/engines/quant/v3/calculations/{id}/units/{unitId}/result',
                'operation_id': 'get_calculation_unit_result_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'unit_id',
                ],
                'required': [
                    'id',
                    'unit_id',
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
                    'unit_id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'unit_id': 'unitId',
                },
                'location_map': {
                    'id': 'path',
                    'unit_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/x-protobuf'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_calculation_unit_result_by_id
        )

        def __post_and_calculate(
            self,
            **kwargs
        ):
            """Create and Run Quant Engine calculation  # noqa: E501

            This endpoint runs the Quant Engine calculation specified in the POST body parameters.  It can take one or more calculation units as input.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_and_calculate(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                cache_control (str): Standard HTTP header.  Accepts no-store, max-age, max-stale.. [optional]
                quant_calculation_parameters_root (QuantCalculationParametersRoot): [optional]
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
                (For 202 status - CalculationStatusRoot)(For 201 status - ObjectRoot)(For 200 status - CalculationStatusRoot)
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

        self.post_and_calculate = _Endpoint(
            settings={
                'response_type': dict({ 202:(CalculationStatusRoot,), 201:(ObjectRoot,), 200:(CalculationStatusRoot,),  }),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/analytics/engines/quant/v3/calculations',
                'operation_id': 'post_and_calculate',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'cache_control',
                    'quant_calculation_parameters_root',
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
                    'cache_control':
                        (str,),
                    'quant_calculation_parameters_root':
                        (QuantCalculationParametersRoot,),
                },
                'attribute_map': {
                    'cache_control': 'Cache-Control',
                },
                'location_map': {
                    'cache_control': 'header',
                    'quant_calculation_parameters_root': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/x-protobuf'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__post_and_calculate
        )

        def __put_and_calculate(
            self,
            id,
            **kwargs
        ):
            """Create or update Quant Engine calculation and run it.  # noqa: E501

            This endpoint updates and runs the Quant Engine calculation specified in the PUT body parameters. This also allows creating new Quant Engine calculations with custom ids.  It can take one or more calculation units as input.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.put_and_calculate(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): from url, provided from the location header in the Create and Run Quant Engine calculation endpoint

            Keyword Args:
                cache_control (str): Standard HTTP header.  Accepts no-store, max-age, max-stale.. [optional]
                quant_calculation_parameters_root (QuantCalculationParametersRoot): Calculation Parameters. [optional]
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
                (For 202 status - CalculationStatusRoot)(For 200 status - CalculationStatusRoot)(For 201 status - ObjectRoot)
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

        self.put_and_calculate = _Endpoint(
            settings={
                'response_type': dict({ 202:(CalculationStatusRoot,), 200:(CalculationStatusRoot,), 201:(ObjectRoot,),  }),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/analytics/engines/quant/v3/calculations/{id}',
                'operation_id': 'put_and_calculate',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'cache_control',
                    'quant_calculation_parameters_root',
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
                    'cache_control':
                        (str,),
                    'quant_calculation_parameters_root':
                        (QuantCalculationParametersRoot,),
                },
                'attribute_map': {
                    'id': 'id',
                    'cache_control': 'Cache-Control',
                },
                'location_map': {
                    'id': 'path',
                    'cache_control': 'header',
                    'quant_calculation_parameters_root': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/x-protobuf'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__put_and_calculate
        )
