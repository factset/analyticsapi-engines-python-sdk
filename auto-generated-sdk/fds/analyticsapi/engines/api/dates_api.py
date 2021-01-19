# coding: utf-8

"""
    Engines API

    Allow clients to fetch Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: v2:[pa,spar,vault,pub],v1:[fiab,fi,axp,afi,npo,bpm,fpo]
    Contact: analytics.api.support@factset.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DatesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def convert_pa_dates_to_absolute_format(self, enddate, componentid, account, **kwargs):  # noqa: E501
        """Convert PA dates to absolute format  # noqa: E501

        This endpoint converts the given start and end dates in FactSet date format to yyyymmdd format for a PA calculation. For more information on FactSet date format, please refer to the PA Engine API documentation under the 'API Documentation' section in the developer portal.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_pa_dates_to_absolute_format(enddate, componentid, account, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str enddate: End Date (required)
        :param str componentid: Component Id (required)
        :param str account: Account (required)
        :param str startdate: Start Date
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DateParametersSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.convert_pa_dates_to_absolute_format_with_http_info(enddate, componentid, account, **kwargs)  # noqa: E501

    def convert_pa_dates_to_absolute_format_with_http_info(self, enddate, componentid, account, **kwargs):  # noqa: E501
        """Convert PA dates to absolute format  # noqa: E501

        This endpoint converts the given start and end dates in FactSet date format to yyyymmdd format for a PA calculation. For more information on FactSet date format, please refer to the PA Engine API documentation under the 'API Documentation' section in the developer portal.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_pa_dates_to_absolute_format_with_http_info(enddate, componentid, account, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str enddate: End Date (required)
        :param str componentid: Component Id (required)
        :param str account: Account (required)
        :param str startdate: Start Date
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DateParametersSummary, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'enddate',
            'componentid',
            'account',
            'startdate'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_pa_dates_to_absolute_format" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'enddate' is set
        if self.api_client.client_side_validation and ('enddate' not in local_var_params or  # noqa: E501
                                                        local_var_params['enddate'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `enddate` when calling `convert_pa_dates_to_absolute_format`")  # noqa: E501
        # verify the required parameter 'componentid' is set
        if self.api_client.client_side_validation and ('componentid' not in local_var_params or  # noqa: E501
                                                        local_var_params['componentid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `componentid` when calling `convert_pa_dates_to_absolute_format`")  # noqa: E501
        # verify the required parameter 'account' is set
        if self.api_client.client_side_validation and ('account' not in local_var_params or  # noqa: E501
                                                        local_var_params['account'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account` when calling `convert_pa_dates_to_absolute_format`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'startdate' in local_var_params and local_var_params['startdate'] is not None:  # noqa: E501
            query_params.append(('startdate', local_var_params['startdate']))  # noqa: E501
        if 'enddate' in local_var_params and local_var_params['enddate'] is not None:  # noqa: E501
            query_params.append(('enddate', local_var_params['enddate']))  # noqa: E501
        if 'componentid' in local_var_params and local_var_params['componentid'] is not None:  # noqa: E501
            query_params.append(('componentid', local_var_params['componentid']))  # noqa: E501
        if 'account' in local_var_params and local_var_params['account'] is not None:  # noqa: E501
            query_params.append(('account', local_var_params['account']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic']  # noqa: E501

        return self.api_client.call_api(
            '/analytics/lookups/v2/engines/pa/dates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DateParametersSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def convert_vault_dates_to_absolute_format(self, enddate, componentid, account, **kwargs):  # noqa: E501
        """Convert Vault dates to absolute format  # noqa: E501

        This endpoint converts the given start and end dates in FactSet date format to yyyymmdd format for a Vault calculation. For more information on FactSet date format, please refer to the Vault API documentation under the 'API Documentation' section in the developer portal.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_vault_dates_to_absolute_format(enddate, componentid, account, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str enddate: End Date (required)
        :param str componentid: Vault Component Id (required)
        :param str account: Account (required)
        :param str startdate: Start Date
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DateParametersSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.convert_vault_dates_to_absolute_format_with_http_info(enddate, componentid, account, **kwargs)  # noqa: E501

    def convert_vault_dates_to_absolute_format_with_http_info(self, enddate, componentid, account, **kwargs):  # noqa: E501
        """Convert Vault dates to absolute format  # noqa: E501

        This endpoint converts the given start and end dates in FactSet date format to yyyymmdd format for a Vault calculation. For more information on FactSet date format, please refer to the Vault API documentation under the 'API Documentation' section in the developer portal.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_vault_dates_to_absolute_format_with_http_info(enddate, componentid, account, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str enddate: End Date (required)
        :param str componentid: Vault Component Id (required)
        :param str account: Account (required)
        :param str startdate: Start Date
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DateParametersSummary, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'enddate',
            'componentid',
            'account',
            'startdate'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_vault_dates_to_absolute_format" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'enddate' is set
        if self.api_client.client_side_validation and ('enddate' not in local_var_params or  # noqa: E501
                                                        local_var_params['enddate'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `enddate` when calling `convert_vault_dates_to_absolute_format`")  # noqa: E501
        # verify the required parameter 'componentid' is set
        if self.api_client.client_side_validation and ('componentid' not in local_var_params or  # noqa: E501
                                                        local_var_params['componentid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `componentid` when calling `convert_vault_dates_to_absolute_format`")  # noqa: E501
        # verify the required parameter 'account' is set
        if self.api_client.client_side_validation and ('account' not in local_var_params or  # noqa: E501
                                                        local_var_params['account'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account` when calling `convert_vault_dates_to_absolute_format`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'startdate' in local_var_params and local_var_params['startdate'] is not None:  # noqa: E501
            query_params.append(('startdate', local_var_params['startdate']))  # noqa: E501
        if 'enddate' in local_var_params and local_var_params['enddate'] is not None:  # noqa: E501
            query_params.append(('enddate', local_var_params['enddate']))  # noqa: E501
        if 'componentid' in local_var_params and local_var_params['componentid'] is not None:  # noqa: E501
            query_params.append(('componentid', local_var_params['componentid']))  # noqa: E501
        if 'account' in local_var_params and local_var_params['account'] is not None:  # noqa: E501
            query_params.append(('account', local_var_params['account']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic']  # noqa: E501

        return self.api_client.call_api(
            '/analytics/lookups/v2/engines/vault/dates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DateParametersSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
