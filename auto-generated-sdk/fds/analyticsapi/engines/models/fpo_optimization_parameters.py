# coding: utf-8

"""
    Engines API

    Allow clients to fetch Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: v3:[pa,spar,vault,pub,fi,axp,afi,npo,bpm,fpo,others],v1:[fiab]
    Contact: analytics.api.support@factset.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fds.analyticsapi.engines.configuration import Configuration


class FPOOptimizationParameters(object):
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
        'account': 'FPOAccount',
        'strategy': 'OptimizerStrategy',
        'optimization': 'Optimization',
        'output_types': 'OptimizerOutputTypes'
    }

    attribute_map = {
        'account': 'account',
        'strategy': 'strategy',
        'optimization': 'optimization',
        'output_types': 'outputTypes'
    }

    def __init__(self, account=None, strategy=None, optimization=None, output_types=None, local_vars_configuration=None):  # noqa: E501
        """FPOOptimizationParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account = None
        self._strategy = None
        self._optimization = None
        self._output_types = None
        self.discriminator = None

        if account is not None:
            self.account = account
        self.strategy = strategy
        if optimization is not None:
            self.optimization = optimization
        self.output_types = output_types

    @property
    def account(self):
        """Gets the account of this FPOOptimizationParameters.  # noqa: E501


        :return: The account of this FPOOptimizationParameters.  # noqa: E501
        :rtype: FPOAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this FPOOptimizationParameters.


        :param account: The account of this FPOOptimizationParameters.  # noqa: E501
        :type: FPOAccount
        """

        self._account = account

    @property
    def strategy(self):
        """Gets the strategy of this FPOOptimizationParameters.  # noqa: E501


        :return: The strategy of this FPOOptimizationParameters.  # noqa: E501
        :rtype: OptimizerStrategy
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """Sets the strategy of this FPOOptimizationParameters.


        :param strategy: The strategy of this FPOOptimizationParameters.  # noqa: E501
        :type: OptimizerStrategy
        """
        if self.local_vars_configuration.client_side_validation and strategy is None:  # noqa: E501
            raise ValueError("Invalid value for `strategy`, must not be `None`")  # noqa: E501

        self._strategy = strategy

    @property
    def optimization(self):
        """Gets the optimization of this FPOOptimizationParameters.  # noqa: E501


        :return: The optimization of this FPOOptimizationParameters.  # noqa: E501
        :rtype: Optimization
        """
        return self._optimization

    @optimization.setter
    def optimization(self, optimization):
        """Sets the optimization of this FPOOptimizationParameters.


        :param optimization: The optimization of this FPOOptimizationParameters.  # noqa: E501
        :type: Optimization
        """

        self._optimization = optimization

    @property
    def output_types(self):
        """Gets the output_types of this FPOOptimizationParameters.  # noqa: E501


        :return: The output_types of this FPOOptimizationParameters.  # noqa: E501
        :rtype: OptimizerOutputTypes
        """
        return self._output_types

    @output_types.setter
    def output_types(self, output_types):
        """Sets the output_types of this FPOOptimizationParameters.


        :param output_types: The output_types of this FPOOptimizationParameters.  # noqa: E501
        :type: OptimizerOutputTypes
        """
        if self.local_vars_configuration.client_side_validation and output_types is None:  # noqa: E501
            raise ValueError("Invalid value for `output_types`, must not be `None`")  # noqa: E501

        self._output_types = output_types

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
        if not isinstance(other, FPOOptimizationParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FPOOptimizationParameters):
            return True

        return self.to_dict() != other.to_dict()
