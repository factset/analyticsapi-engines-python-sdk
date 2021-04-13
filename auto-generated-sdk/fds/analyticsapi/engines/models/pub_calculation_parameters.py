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


class PubCalculationParameters(object):
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
        'document': 'str',
        'account': 'PubIdentifier',
        'dates': 'PubDateParameters'
    }

    attribute_map = {
        'document': 'document',
        'account': 'account',
        'dates': 'dates'
    }

    def __init__(self, document=None, account=None, dates=None, local_vars_configuration=None):  # noqa: E501
        """PubCalculationParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._document = None
        self._account = None
        self._dates = None
        self.discriminator = None

        self.document = document
        self.account = account
        self.dates = dates

    @property
    def document(self):
        """Gets the document of this PubCalculationParameters.  # noqa: E501

        The Publisher Engine document to analyze.  # noqa: E501

        :return: The document of this PubCalculationParameters.  # noqa: E501
        :rtype: str
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this PubCalculationParameters.

        The Publisher Engine document to analyze.  # noqa: E501

        :param document: The document of this PubCalculationParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and document is None:  # noqa: E501
            raise ValueError("Invalid value for `document`, must not be `None`")  # noqa: E501

        self._document = document

    @property
    def account(self):
        """Gets the account of this PubCalculationParameters.  # noqa: E501


        :return: The account of this PubCalculationParameters.  # noqa: E501
        :rtype: PubIdentifier
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this PubCalculationParameters.


        :param account: The account of this PubCalculationParameters.  # noqa: E501
        :type: PubIdentifier
        """
        if self.local_vars_configuration.client_side_validation and account is None:  # noqa: E501
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def dates(self):
        """Gets the dates of this PubCalculationParameters.  # noqa: E501


        :return: The dates of this PubCalculationParameters.  # noqa: E501
        :rtype: PubDateParameters
        """
        return self._dates

    @dates.setter
    def dates(self, dates):
        """Sets the dates of this PubCalculationParameters.


        :param dates: The dates of this PubCalculationParameters.  # noqa: E501
        :type: PubDateParameters
        """
        if self.local_vars_configuration.client_side_validation and dates is None:  # noqa: E501
            raise ValueError("Invalid value for `dates`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, PubCalculationParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PubCalculationParameters):
            return True

        return self.to_dict() != other.to_dict()
