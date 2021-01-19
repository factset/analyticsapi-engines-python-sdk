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


class ConfigurationAccount(object):
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
        'benchmark_code': 'str',
        'benchmark_name': 'str',
        'max_end_date': 'str',
        'min_start_date': 'str',
        'locking_date': 'str',
        'name': 'str'
    }

    attribute_map = {
        'benchmark_code': 'benchmarkCode',
        'benchmark_name': 'benchmarkName',
        'max_end_date': 'maxEndDate',
        'min_start_date': 'minStartDate',
        'locking_date': 'lockingDate',
        'name': 'name'
    }

    def __init__(self, benchmark_code=None, benchmark_name=None, max_end_date=None, min_start_date=None, locking_date=None, name=None, local_vars_configuration=None):  # noqa: E501
        """ConfigurationAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._benchmark_code = None
        self._benchmark_name = None
        self._max_end_date = None
        self._min_start_date = None
        self._locking_date = None
        self._name = None
        self.discriminator = None

        if benchmark_code is not None:
            self.benchmark_code = benchmark_code
        if benchmark_name is not None:
            self.benchmark_name = benchmark_name
        if max_end_date is not None:
            self.max_end_date = max_end_date
        if min_start_date is not None:
            self.min_start_date = min_start_date
        if locking_date is not None:
            self.locking_date = locking_date
        if name is not None:
            self.name = name

    @property
    def benchmark_code(self):
        """Gets the benchmark_code of this ConfigurationAccount.  # noqa: E501

        Benchmark code.  # noqa: E501

        :return: The benchmark_code of this ConfigurationAccount.  # noqa: E501
        :rtype: str
        """
        return self._benchmark_code

    @benchmark_code.setter
    def benchmark_code(self, benchmark_code):
        """Sets the benchmark_code of this ConfigurationAccount.

        Benchmark code.  # noqa: E501

        :param benchmark_code: The benchmark_code of this ConfigurationAccount.  # noqa: E501
        :type: str
        """

        self._benchmark_code = benchmark_code

    @property
    def benchmark_name(self):
        """Gets the benchmark_name of this ConfigurationAccount.  # noqa: E501

        Benchmark name.  # noqa: E501

        :return: The benchmark_name of this ConfigurationAccount.  # noqa: E501
        :rtype: str
        """
        return self._benchmark_name

    @benchmark_name.setter
    def benchmark_name(self, benchmark_name):
        """Sets the benchmark_name of this ConfigurationAccount.

        Benchmark name.  # noqa: E501

        :param benchmark_name: The benchmark_name of this ConfigurationAccount.  # noqa: E501
        :type: str
        """

        self._benchmark_name = benchmark_name

    @property
    def max_end_date(self):
        """Gets the max_end_date of this ConfigurationAccount.  # noqa: E501

        Maximum end date.  # noqa: E501

        :return: The max_end_date of this ConfigurationAccount.  # noqa: E501
        :rtype: str
        """
        return self._max_end_date

    @max_end_date.setter
    def max_end_date(self, max_end_date):
        """Sets the max_end_date of this ConfigurationAccount.

        Maximum end date.  # noqa: E501

        :param max_end_date: The max_end_date of this ConfigurationAccount.  # noqa: E501
        :type: str
        """

        self._max_end_date = max_end_date

    @property
    def min_start_date(self):
        """Gets the min_start_date of this ConfigurationAccount.  # noqa: E501

        Minimum start date.  # noqa: E501

        :return: The min_start_date of this ConfigurationAccount.  # noqa: E501
        :rtype: str
        """
        return self._min_start_date

    @min_start_date.setter
    def min_start_date(self, min_start_date):
        """Sets the min_start_date of this ConfigurationAccount.

        Minimum start date.  # noqa: E501

        :param min_start_date: The min_start_date of this ConfigurationAccount.  # noqa: E501
        :type: str
        """

        self._min_start_date = min_start_date

    @property
    def locking_date(self):
        """Gets the locking_date of this ConfigurationAccount.  # noqa: E501

        Locking date.  # noqa: E501

        :return: The locking_date of this ConfigurationAccount.  # noqa: E501
        :rtype: str
        """
        return self._locking_date

    @locking_date.setter
    def locking_date(self, locking_date):
        """Sets the locking_date of this ConfigurationAccount.

        Locking date.  # noqa: E501

        :param locking_date: The locking_date of this ConfigurationAccount.  # noqa: E501
        :type: str
        """

        self._locking_date = locking_date

    @property
    def name(self):
        """Gets the name of this ConfigurationAccount.  # noqa: E501

        Account name.  # noqa: E501

        :return: The name of this ConfigurationAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigurationAccount.

        Account name.  # noqa: E501

        :param name: The name of this ConfigurationAccount.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, ConfigurationAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigurationAccount):
            return True

        return self.to_dict() != other.to_dict()
