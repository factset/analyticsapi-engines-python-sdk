"""
    Engines API

    Allow clients to fetch Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: v3:[pa,vault,pub,quant,fi,axp,afi,npo,bpm,fpo,security-modeling,others],v1:[fiab]
    Contact: api@factset.com
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
from fds.analyticsapi.engines.model.client_error_response import ClientErrorResponse
from fds.analyticsapi.engines.model.sm_create_parameters_root import SMCreateParametersRoot
from fds.analyticsapi.engines.model.sm_create_response_root import SMCreateResponseRoot
from fds.analyticsapi.engines.model.sm_delete_parameters_root import SMDeleteParametersRoot
from fds.analyticsapi.engines.model.sm_delete_response_root import SMDeleteResponseRoot
from fds.analyticsapi.engines.model.sm_retrieve_parameters_root import SMRetrieveParametersRoot
from fds.analyticsapi.engines.model.sm_retrieve_response_root import SMRetrieveResponseRoot
from fds.analyticsapi.engines.model.sm_template_field_properties_root import SMTemplateFieldPropertiesRoot


class SecurityModelingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __delete_securities(
            self,
            **kwargs
        ):
            """Delete existing securities  # noqa: E501

            This endpoint deletes existing securities.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_securities(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                sm_delete_parameters_root (SMDeleteParametersRoot): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
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
                SMDeleteResponseRoot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
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

        self.delete_securities = _Endpoint(
            settings={
                'response_type': dict({ 200:(SMDeleteResponseRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/security-modeling/v3/securities/delete',
                'operation_id': 'delete_securities',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'sm_delete_parameters_root',
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
                    'sm_delete_parameters_root':
                        (SMDeleteParametersRoot,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'sm_delete_parameters_root': 'body',
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
            callable=__delete_securities
        )

        def __get_securities(
            self,
            **kwargs
        ):
            """Get existing securities  # noqa: E501

            This endpoint gets all existing securities.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_securities(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                sm_retrieve_parameters_root (SMRetrieveParametersRoot): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
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
                SMRetrieveResponseRoot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
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

        self.get_securities = _Endpoint(
            settings={
                'response_type': dict({ 200:(SMRetrieveResponseRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/security-modeling/v3/securities/retrieve',
                'operation_id': 'get_securities',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'sm_retrieve_parameters_root',
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
                    'sm_retrieve_parameters_root':
                        (SMRetrieveParametersRoot,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'sm_retrieve_parameters_root': 'body',
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
            callable=__get_securities
        )

        def __get_template_fields(
            self,
            template,
            **kwargs
        ):
            """Get template fields  # noqa: E501

            This endpoint gets template fields.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_template_fields(template, async_req=True)
            >>> result = thread.get()

            Args:
                template (str): Template name

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
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
                SMTemplateFieldPropertiesRoot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
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
            kwargs['template'] = \
                template
            return self.call_with_http_info(**kwargs)

        self.get_template_fields = _Endpoint(
            settings={
                'response_type': dict({ 200:(SMTemplateFieldPropertiesRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/security-modeling/v3/templates/{template}/fields',
                'operation_id': 'get_template_fields',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'template',
                ],
                'required': [
                    'template',
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
                    'template':
                        (str,),
                },
                'attribute_map': {
                    'template': 'template',
                },
                'location_map': {
                    'template': 'path',
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
            callable=__get_template_fields
        )

        def __upsert_securities(
            self,
            **kwargs
        ):
            """Create or update securities  # noqa: E501

            This endpoint is to create or update existing securities.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.upsert_securities(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                sm_create_parameters_root (SMCreateParametersRoot): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
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
                SMCreateResponseRoot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
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

        self.upsert_securities = _Endpoint(
            settings={
                'response_type': dict({ 200:(SMCreateResponseRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/security-modeling/v3/securities/upsert',
                'operation_id': 'upsert_securities',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'sm_create_parameters_root',
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
                    'sm_create_parameters_root':
                        (SMCreateParametersRoot,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'sm_create_parameters_root': 'body',
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
            callable=__upsert_securities
        )
