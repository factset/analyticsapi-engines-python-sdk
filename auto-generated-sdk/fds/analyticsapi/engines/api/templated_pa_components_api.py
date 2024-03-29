"""
    Engines API

    Allow clients to fetch Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: v3:[pa,spar,vault,pub,quant,fi,axp,afi,npo,bpm,fpo,others],v1:[fiab]
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
from fds.analyticsapi.engines.model.templated_pa_component_parameters_root import TemplatedPAComponentParametersRoot
from fds.analyticsapi.engines.model.templated_pa_component_post_summary_root import TemplatedPAComponentPostSummaryRoot
from fds.analyticsapi.engines.model.templated_pa_component_root import TemplatedPAComponentRoot
from fds.analyticsapi.engines.model.templated_pa_component_summary_root import TemplatedPAComponentSummaryRoot
from fds.analyticsapi.engines.model.templated_pa_component_update_parameters_root import TemplatedPAComponentUpdateParametersRoot


class TemplatedPAComponentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_templated_pa_components(
            self,
            templated_pa_component_parameters_root,
            **kwargs
        ):
            """Create templated PA component  # noqa: E501

            This endpoint creates new component based off of linked PA template or unlinked PA template.    Remarks:    *   Any settings in the POST body will act as a one-time override over the settings saved in the PA template.    *   Account identifiers must have .ACCT or .ACTM extension or BENCH: prefix. Holdings mode can be optionally set for every account.       Possible values for holdings mode are B&H (Buy and Hold), TBR (Transaction based returns), OMS (Order Management System),       VLT (Vaulted returns) or EXT (External Returns Data). Default holdings mode value is B&H.    *   Multi-horizon frequencies are not supported through this endpoint.    *   Componentdetail supports securities, groups, groupsall, and totals levels of granularity. However, if no value is passed, the default value is 'securities'.      Additionally, while 'groupsall' returns all the group levels in the PA component,      setting componentdetail to 'groups' only returns the expanded or collapsed group levels within the PA component.    *   If we are overriding the grouping with a frequency, we will be overriding the grouping saved to the original component and also overriding       the default frequency of the Beginning of Period to whatever we pass in the request body.        *   If we are overriding grouping frequency without overriding the group id it will not be applied to the default groupings saved to the original component.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_templated_pa_components(templated_pa_component_parameters_root, async_req=True)
            >>> result = thread.get()

            Args:
                templated_pa_component_parameters_root (TemplatedPAComponentParametersRoot): Request Parameters

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
                TemplatedPAComponentPostSummaryRoot
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
            kwargs['templated_pa_component_parameters_root'] = \
                templated_pa_component_parameters_root
            return self.call_with_http_info(**kwargs)

        self.create_templated_pa_components = _Endpoint(
            settings={
                'response_type': dict({ 201:(TemplatedPAComponentPostSummaryRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pa/v3/templated-components',
                'operation_id': 'create_templated_pa_components',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'templated_pa_component_parameters_root',
                ],
                'required': [
                    'templated_pa_component_parameters_root',
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
                    'templated_pa_component_parameters_root':
                        (TemplatedPAComponentParametersRoot,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'templated_pa_component_parameters_root': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_templated_pa_components
        )

        def __delete_templated_pa_components(
            self,
            id,
            **kwargs
        ):
            """Delete templated PA component  # noqa: E501

            This endpoint deletes an existing templated PA component  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_templated_pa_components(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Unique identifier for a templated PA component

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
                None
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
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.delete_templated_pa_components = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pa/v3/templated-components/{id}',
                'operation_id': 'delete_templated_pa_components',
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
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_templated_pa_components
        )

        def __get_templated_pa_component_by_id(
            self,
            id,
            **kwargs
        ):
            """Get templated PA component by id  # noqa: E501

            This endpoint fetches the templated PA component settings.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_templated_pa_component_by_id(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Unique identifier for a templated PA component

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
                TemplatedPAComponentRoot
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
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.get_templated_pa_component_by_id = _Endpoint(
            settings={
                'response_type': dict({ 200:(TemplatedPAComponentRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pa/v3/templated-components/{id}',
                'operation_id': 'get_templated_pa_component_by_id',
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
            callable=__get_templated_pa_component_by_id
        )

        def __get_templated_pa_components_in_path(
            self,
            directory,
            **kwargs
        ):
            """Get templated PA components in path  # noqa: E501

            This endpoint returns the list of templated PA components in path.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_templated_pa_components_in_path(directory, async_req=True)
            >>> result = thread.get()

            Args:
                directory (str): Get templated PA components in path

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
                TemplatedPAComponentSummaryRoot
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
            kwargs['directory'] = \
                directory
            return self.call_with_http_info(**kwargs)

        self.get_templated_pa_components_in_path = _Endpoint(
            settings={
                'response_type': dict({ 200:(TemplatedPAComponentSummaryRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pa/v3/templated-components',
                'operation_id': 'get_templated_pa_components_in_path',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'directory',
                ],
                'required': [
                    'directory',
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
                    'directory':
                        (str,),
                },
                'attribute_map': {
                    'directory': 'directory',
                },
                'location_map': {
                    'directory': 'query',
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
            callable=__get_templated_pa_components_in_path
        )

        def __update_templated_pa_components(
            self,
            id,
            templated_pa_component_update_parameters_root,
            **kwargs
        ):
            """Update templated PA component  # noqa: E501

            This endpoint allows the user to change the request body from an existing templated PA component.    Remarks:    *   Any settings in the POST body will act as a one-time override over the settings saved in the PA template.    *   Account identifiers must have .ACCT or .ACTM extension or BENCH: prefix. Holdings mode can be optionally set for every account.       Possible values for holdings mode are B&H (Buy and Hold), TBR (Transaction based returns), OMS (Order Management System),       VLT (Vaulted returns) or EXT (External Returns Data). Default holdings mode value is B&H.     *   Multi-horizon frequencies are not supported through this endpoint.    *   Componentdetail supports securities, groups, groupsall, and totals levels of granularity. However, if no value is passed, the default value is 'securities'.      Additionally, while 'groupsall' returns all the group levels in the PA component,      setting componentdetail to 'groups' only returns the expanded or collapsed group levels within the PA component.    *   If we are overriding the grouping with a frequency, we will be overriding the grouping saved to the original component and also overriding       the default frequency of the Beginning of Period to whatever we pass in the request body.        *   If we are overriding grouping frequency without overriding the group id it will not be applied to the default groupings saved to the original component.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_templated_pa_components(id, templated_pa_component_update_parameters_root, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Unique identifier for a templated PA component
                templated_pa_component_update_parameters_root (TemplatedPAComponentUpdateParametersRoot): Request Parameters

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
                TemplatedPAComponentPostSummaryRoot
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
            kwargs['id'] = \
                id
            kwargs['templated_pa_component_update_parameters_root'] = \
                templated_pa_component_update_parameters_root
            return self.call_with_http_info(**kwargs)

        self.update_templated_pa_components = _Endpoint(
            settings={
                'response_type': dict({ 200:(TemplatedPAComponentPostSummaryRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pa/v3/templated-components/{id}',
                'operation_id': 'update_templated_pa_components',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'templated_pa_component_update_parameters_root',
                ],
                'required': [
                    'id',
                    'templated_pa_component_update_parameters_root',
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
                    'templated_pa_component_update_parameters_root':
                        (TemplatedPAComponentUpdateParametersRoot,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                    'templated_pa_component_update_parameters_root': 'body',
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
            callable=__update_templated_pa_components
        )
