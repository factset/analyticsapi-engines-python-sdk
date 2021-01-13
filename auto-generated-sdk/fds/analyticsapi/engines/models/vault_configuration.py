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


class VaultConfiguration(object):
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
        'name': 'str',
        'accounts': 'dict(str, ConfigurationAccount)'
    }

    attribute_map = {
        'name': 'name',
        'accounts': 'accounts'
    }

    def __init__(self, name=None, accounts=None, local_vars_configuration=None):  # noqa: E501
        """VaultConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._accounts = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if accounts is not None:
            self.accounts = accounts

    @property
    def name(self):
        """Gets the name of this VaultConfiguration.  # noqa: E501

        Configuration name.  # noqa: E501

        :return: The name of this VaultConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VaultConfiguration.

        Configuration name.  # noqa: E501

        :param name: The name of this VaultConfiguration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def accounts(self):
        """Gets the accounts of this VaultConfiguration.  # noqa: E501


        :return: The accounts of this VaultConfiguration.  # noqa: E501
        :rtype: dict(str, ConfigurationAccount)
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this VaultConfiguration.


        :param accounts: The accounts of this VaultConfiguration.  # noqa: E501
        :type: dict(str, ConfigurationAccount)
        """

        self._accounts = accounts

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
        if not isinstance(other, VaultConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VaultConfiguration):
            return True

        return self.to_dict() != other.to_dict()
