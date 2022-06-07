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
from fds.analyticsapi.engines.model.client_error_response import ClientErrorResponse
from fds.analyticsapi.engines.model.pa_pricing_source_root import PAPricingSourceRoot


class PricingSourcesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_pa_pricing_sources(
            self,
            **kwargs
        ):
            """Get PA pricing sources  # noqa: E501

            This endpoint lists all the PA pricing sources that can be applied to a PA calculation.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_pa_pricing_sources(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                name (str): PA pricing sources name. [optional] if omitted the server will use the default value of ""
                category (str): PA pricing sources category. [optional] if omitted the server will use the default value of ""
                directory (str): The directory to get the PA pricing sources in. [optional] if omitted the server will use the default value of ""
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
                PAPricingSourceRoot
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

        self.get_pa_pricing_sources = _Endpoint(
            settings={
                'response_type': dict({ 200:(PAPricingSourceRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pa/v3/pricing-sources',
                'operation_id': 'get_pa_pricing_sources',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'category',
                    'directory',
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
                    'name':
                        (str,),
                    'category':
                        (str,),
                    'directory':
                        (str,),
                },
                'attribute_map': {
                    'name': 'name',
                    'category': 'category',
                    'directory': 'directory',
                },
                'location_map': {
                    'name': 'query',
                    'category': 'query',
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
            callable=__get_pa_pricing_sources
        )
