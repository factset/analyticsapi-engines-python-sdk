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


class OptimizerAccountOverrides(object):
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
        'portfolio': 'str',
        'benchmark': 'str',
        'riskmodelid': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'portfolio': 'portfolio',
        'benchmark': 'benchmark',
        'riskmodelid': 'riskmodelid',
        'currency': 'currency'
    }

    def __init__(self, portfolio=None, benchmark=None, riskmodelid=None, currency=None, local_vars_configuration=None):  # noqa: E501
        """OptimizerAccountOverrides - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._portfolio = None
        self._benchmark = None
        self._riskmodelid = None
        self._currency = None
        self.discriminator = None

        if portfolio is not None:
            self.portfolio = portfolio
        if benchmark is not None:
            self.benchmark = benchmark
        if riskmodelid is not None:
            self.riskmodelid = riskmodelid
        if currency is not None:
            self.currency = currency

    @property
    def portfolio(self):
        """Gets the portfolio of this OptimizerAccountOverrides.  # noqa: E501

        Portfolio  # noqa: E501

        :return: The portfolio of this OptimizerAccountOverrides.  # noqa: E501
        :rtype: str
        """
        return self._portfolio

    @portfolio.setter
    def portfolio(self, portfolio):
        """Sets the portfolio of this OptimizerAccountOverrides.

        Portfolio  # noqa: E501

        :param portfolio: The portfolio of this OptimizerAccountOverrides.  # noqa: E501
        :type: str
        """

        self._portfolio = portfolio

    @property
    def benchmark(self):
        """Gets the benchmark of this OptimizerAccountOverrides.  # noqa: E501

        Benchmark  # noqa: E501

        :return: The benchmark of this OptimizerAccountOverrides.  # noqa: E501
        :rtype: str
        """
        return self._benchmark

    @benchmark.setter
    def benchmark(self, benchmark):
        """Sets the benchmark of this OptimizerAccountOverrides.

        Benchmark  # noqa: E501

        :param benchmark: The benchmark of this OptimizerAccountOverrides.  # noqa: E501
        :type: str
        """

        self._benchmark = benchmark

    @property
    def riskmodelid(self):
        """Gets the riskmodelid of this OptimizerAccountOverrides.  # noqa: E501

        Risk model  # noqa: E501

        :return: The riskmodelid of this OptimizerAccountOverrides.  # noqa: E501
        :rtype: str
        """
        return self._riskmodelid

    @riskmodelid.setter
    def riskmodelid(self, riskmodelid):
        """Sets the riskmodelid of this OptimizerAccountOverrides.

        Risk model  # noqa: E501

        :param riskmodelid: The riskmodelid of this OptimizerAccountOverrides.  # noqa: E501
        :type: str
        """

        self._riskmodelid = riskmodelid

    @property
    def currency(self):
        """Gets the currency of this OptimizerAccountOverrides.  # noqa: E501

        Currency  # noqa: E501

        :return: The currency of this OptimizerAccountOverrides.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this OptimizerAccountOverrides.

        Currency  # noqa: E501

        :param currency: The currency of this OptimizerAccountOverrides.  # noqa: E501
        :type: str
        """

        self._currency = currency

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
        if not isinstance(other, OptimizerAccountOverrides):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OptimizerAccountOverrides):
            return True

        return self.to_dict() != other.to_dict()
