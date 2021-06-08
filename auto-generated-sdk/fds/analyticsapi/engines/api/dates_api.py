"""
    Engines API

    Allow clients to fetch Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: v3:[pa,spar,vault,pub,fi,axp,afi,npo,bpm,fpo,others],v1:[fiab]
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
from fds.analyticsapi.engines.model.date_parameters_summary_root import DateParametersSummaryRoot


class DatesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __convert_pa_dates_to_absolute_format(
            self,
            enddate,
            componentid,
            account,
            **kwargs
        ):
            """Convert PA dates to absolute format  # noqa: E501

            This endpoint converts the given start and end dates in FactSet date format to yyyymmdd format for a PA calculation. For more information on FactSet date format, please refer to the PA Engine API documentation under the 'API Documentation' section in the developer portal.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.convert_pa_dates_to_absolute_format(enddate, componentid, account, async_req=True)
            >>> result = thread.get()

            Args:
                enddate (str): End Date
                componentid (str): Component Id
                account (str): Account

            Keyword Args:
                startdate (str): Start Date. [optional]
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
                DateParametersSummaryRoot
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
            kwargs['enddate'] = \
                enddate
            kwargs['componentid'] = \
                componentid
            kwargs['account'] = \
                account
            return self.call_with_http_info(**kwargs)

        self.convert_pa_dates_to_absolute_format = _Endpoint(
            settings={
                'response_type': dict({ 200:(DateParametersSummaryRoot,),  }),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/analytics/engines/pa/v3/dates',
                'operation_id': 'convert_pa_dates_to_absolute_format',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'enddate',
                    'componentid',
                    'account',
                    'startdate',
                ],
                'required': [
                    'enddate',
                    'componentid',
                    'account',
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
                    'enddate':
                        (str,),
                    'componentid':
                        (str,),
                    'account':
                        (str,),
                    'startdate':
                        (str,),
                },
                'attribute_map': {
                    'enddate': 'enddate',
                    'componentid': 'componentid',
                    'account': 'account',
                    'startdate': 'startdate',
                },
                'location_map': {
                    'enddate': 'query',
                    'componentid': 'query',
                    'account': 'query',
                    'startdate': 'query',
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
            callable=__convert_pa_dates_to_absolute_format
        )

        def __convert_vault_dates_to_absolute_format(
            self,
            enddate,
            componentid,
            account,
            **kwargs
        ):
            """Convert Vault dates to absolute format  # noqa: E501

            This endpoint converts the given start and end dates in FactSet date format to yyyymmdd format for a Vault calculation. For more information on FactSet date format, please refer to the Vault API documentation under the 'API Documentation' section in the developer portal.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.convert_vault_dates_to_absolute_format(enddate, componentid, account, async_req=True)
            >>> result = thread.get()

            Args:
                enddate (str): End Date
                componentid (str): Vault Component Id
                account (str): Account

            Keyword Args:
                startdate (str): Start Date. [optional]
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
                DateParametersSummaryRoot
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
            kwargs['enddate'] = \
                enddate
            kwargs['componentid'] = \
                componentid
            kwargs['account'] = \
                account
            return self.call_with_http_info(**kwargs)

        self.convert_vault_dates_to_absolute_format = _Endpoint(
            settings={
                'response_type': dict({ 200:(DateParametersSummaryRoot,),  }),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/analytics/engines/vault/v3/dates',
                'operation_id': 'convert_vault_dates_to_absolute_format',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'enddate',
                    'componentid',
                    'account',
                    'startdate',
                ],
                'required': [
                    'enddate',
                    'componentid',
                    'account',
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
                    'enddate':
                        (str,),
                    'componentid':
                        (str,),
                    'account':
                        (str,),
                    'startdate':
                        (str,),
                },
                'attribute_map': {
                    'enddate': 'enddate',
                    'componentid': 'componentid',
                    'account': 'account',
                    'startdate': 'startdate',
                },
                'location_map': {
                    'enddate': 'query',
                    'componentid': 'query',
                    'account': 'query',
                    'startdate': 'query',
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
            callable=__convert_vault_dates_to_absolute_format
        )
