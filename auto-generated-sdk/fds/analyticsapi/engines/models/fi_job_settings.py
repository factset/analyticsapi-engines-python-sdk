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


class FIJobSettings(object):
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
        'as_of_date': 'str',
        'partial_duration_months': 'list[int]'
    }

    attribute_map = {
        'as_of_date': 'asOfDate',
        'partial_duration_months': 'partialDurationMonths'
    }

    def __init__(self, as_of_date=None, partial_duration_months=None, local_vars_configuration=None):  # noqa: E501
        """FIJobSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._as_of_date = None
        self._partial_duration_months = None
        self.discriminator = None

        self.as_of_date = as_of_date
        if partial_duration_months is not None:
            self.partial_duration_months = partial_duration_months

    @property
    def as_of_date(self):
        """Gets the as_of_date of this FIJobSettings.  # noqa: E501


        :return: The as_of_date of this FIJobSettings.  # noqa: E501
        :rtype: str
        """
        return self._as_of_date

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this FIJobSettings.


        :param as_of_date: The as_of_date of this FIJobSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and as_of_date is None:  # noqa: E501
            raise ValueError("Invalid value for `as_of_date`, must not be `None`")  # noqa: E501

        self._as_of_date = as_of_date

    @property
    def partial_duration_months(self):
        """Gets the partial_duration_months of this FIJobSettings.  # noqa: E501


        :return: The partial_duration_months of this FIJobSettings.  # noqa: E501
        :rtype: list[int]
        """
        return self._partial_duration_months

    @partial_duration_months.setter
    def partial_duration_months(self, partial_duration_months):
        """Sets the partial_duration_months of this FIJobSettings.


        :param partial_duration_months: The partial_duration_months of this FIJobSettings.  # noqa: E501
        :type: list[int]
        """

        self._partial_duration_months = partial_duration_months

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
        if not isinstance(other, FIJobSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FIJobSettings):
            return True

        return self.to_dict() != other.to_dict()
