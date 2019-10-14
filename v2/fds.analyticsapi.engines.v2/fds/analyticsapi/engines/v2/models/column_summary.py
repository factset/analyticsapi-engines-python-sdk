# coding: utf-8

"""
    Engines API

    Allow clients to fetch Engines Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: 2
    Contact: analytics.api.support@factset.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ColumnSummary(object):
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
        'directory': 'str',
        'category': 'str'
    }

    attribute_map = {
        'name': 'name',
        'directory': 'directory',
        'category': 'category'
    }

    def __init__(self, name=None, directory=None, category=None):  # noqa: E501
        """ColumnSummary - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._directory = None
        self._category = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if directory is not None:
            self.directory = directory
        if category is not None:
            self.category = category

    @property
    def name(self):
        """Gets the name of this ColumnSummary.  # noqa: E501

        Column Name  # noqa: E501

        :return: The name of this ColumnSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ColumnSummary.

        Column Name  # noqa: E501

        :param name: The name of this ColumnSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def directory(self):
        """Gets the directory of this ColumnSummary.  # noqa: E501

        Column Directory  # noqa: E501

        :return: The directory of this ColumnSummary.  # noqa: E501
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this ColumnSummary.

        Column Directory  # noqa: E501

        :param directory: The directory of this ColumnSummary.  # noqa: E501
        :type: str
        """

        self._directory = directory

    @property
    def category(self):
        """Gets the category of this ColumnSummary.  # noqa: E501

        Column Category  # noqa: E501

        :return: The category of this ColumnSummary.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ColumnSummary.

        Column Category  # noqa: E501

        :param category: The category of this ColumnSummary.  # noqa: E501
        :type: str
        """

        self._category = category

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
        if not isinstance(other, ColumnSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
