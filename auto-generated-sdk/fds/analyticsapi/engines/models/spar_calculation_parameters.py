# coding: utf-8

"""
    Engines API

    Allow clients to fetch Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: v2:[pa,spar,vault,pub],v1:[fiab,fi,axp,afi,npo,bpm,fpo]
    Contact: analytics.api.support@factset.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fds.analyticsapi.engines.configuration import Configuration


class SPARCalculationParameters(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'componentid': 'str',
        'accounts': 'list[SPARIdentifier]',
        'benchmark': 'SPARIdentifier',
        'dates': 'SPARDateParameters'
    }

    attribute_map = {
        'componentid': 'componentid',
        'accounts': 'accounts',
        'benchmark': 'benchmark',
        'dates': 'dates'
    }

    def __init__(self, componentid=None, accounts=None, benchmark=None, dates=None, local_vars_configuration=None):  # noqa: E501
        """SPARCalculationParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._componentid = None
        self._accounts = None
        self._benchmark = None
        self._dates = None
        self.discriminator = None

        self.componentid = componentid
        if accounts is not None:
            self.accounts = accounts
        if benchmark is not None:
            self.benchmark = benchmark
        if dates is not None:
            self.dates = dates

    @property
    def componentid(self):
        """Gets the componentid of this SPARCalculationParameters.  # noqa: E501

        The SPAR Engine component identifier to analyze.  # noqa: E501

        :return: The componentid of this SPARCalculationParameters.  # noqa: E501
        :rtype: str
        """
        return self._componentid

    @componentid.setter
    def componentid(self, componentid):
        """Sets the componentid of this SPARCalculationParameters.

        The SPAR Engine component identifier to analyze.  # noqa: E501

        :param componentid: The componentid of this SPARCalculationParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and componentid is None:  # noqa: E501
            raise ValueError("Invalid value for `componentid`, must not be `None`")  # noqa: E501

        self._componentid = componentid

    @property
    def accounts(self):
        """Gets the accounts of this SPARCalculationParameters.  # noqa: E501

        List of accounts for SPAR calculation.  # noqa: E501

        :return: The accounts of this SPARCalculationParameters.  # noqa: E501
        :rtype: list[SPARIdentifier]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this SPARCalculationParameters.

        List of accounts for SPAR calculation.  # noqa: E501

        :param accounts: The accounts of this SPARCalculationParameters.  # noqa: E501
        :type: list[SPARIdentifier]
        """

        self._accounts = accounts

    @property
    def benchmark(self):
        """Gets the benchmark of this SPARCalculationParameters.  # noqa: E501


        :return: The benchmark of this SPARCalculationParameters.  # noqa: E501
        :rtype: SPARIdentifier
        """
        return self._benchmark

    @benchmark.setter
    def benchmark(self, benchmark):
        """Sets the benchmark of this SPARCalculationParameters.


        :param benchmark: The benchmark of this SPARCalculationParameters.  # noqa: E501
        :type: SPARIdentifier
        """

        self._benchmark = benchmark

    @property
    def dates(self):
        """Gets the dates of this SPARCalculationParameters.  # noqa: E501


        :return: The dates of this SPARCalculationParameters.  # noqa: E501
        :rtype: SPARDateParameters
        """
        return self._dates

    @dates.setter
    def dates(self, dates):
        """Sets the dates of this SPARCalculationParameters.


        :param dates: The dates of this SPARCalculationParameters.  # noqa: E501
        :type: SPARDateParameters
        """

        self._dates = dates

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SPARCalculationParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SPARCalculationParameters):
            return True

        return self.to_dict() != other.to_dict()
