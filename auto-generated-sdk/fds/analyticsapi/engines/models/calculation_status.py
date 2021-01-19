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


class CalculationStatus(object):
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
        'status': 'str',
        'units': 'int',
        'pa': 'dict(str, CalculationUnitStatus)',
        'spar': 'dict(str, CalculationUnitStatus)',
        'vault': 'dict(str, CalculationUnitStatus)',
        'pub': 'dict(str, CalculationUnitStatus)'
    }

    attribute_map = {
        'status': 'status',
        'units': 'units',
        'pa': 'pa',
        'spar': 'spar',
        'vault': 'vault',
        'pub': 'pub'
    }

    def __init__(self, status=None, units=None, pa=None, spar=None, vault=None, pub=None, local_vars_configuration=None):  # noqa: E501
        """CalculationStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._units = None
        self._pa = None
        self._spar = None
        self._vault = None
        self._pub = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if units is not None:
            self.units = units
        if pa is not None:
            self.pa = pa
        if spar is not None:
            self.spar = spar
        if vault is not None:
            self.vault = vault
        if pub is not None:
            self.pub = pub

    @property
    def status(self):
        """Gets the status of this CalculationStatus.  # noqa: E501


        :return: The status of this CalculationStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CalculationStatus.


        :param status: The status of this CalculationStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["Queued", "Executing", "Completed", "Cancelled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def units(self):
        """Gets the units of this CalculationStatus.  # noqa: E501

        Number of calculation units in batch.  # noqa: E501

        :return: The units of this CalculationStatus.  # noqa: E501
        :rtype: int
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this CalculationStatus.

        Number of calculation units in batch.  # noqa: E501

        :param units: The units of this CalculationStatus.  # noqa: E501
        :type: int
        """

        self._units = units

    @property
    def pa(self):
        """Gets the pa of this CalculationStatus.  # noqa: E501

        List of statuses for PA calculation units.  # noqa: E501

        :return: The pa of this CalculationStatus.  # noqa: E501
        :rtype: dict(str, CalculationUnitStatus)
        """
        return self._pa

    @pa.setter
    def pa(self, pa):
        """Sets the pa of this CalculationStatus.

        List of statuses for PA calculation units.  # noqa: E501

        :param pa: The pa of this CalculationStatus.  # noqa: E501
        :type: dict(str, CalculationUnitStatus)
        """

        self._pa = pa

    @property
    def spar(self):
        """Gets the spar of this CalculationStatus.  # noqa: E501

        List of statuses for SPAR calculation units.  # noqa: E501

        :return: The spar of this CalculationStatus.  # noqa: E501
        :rtype: dict(str, CalculationUnitStatus)
        """
        return self._spar

    @spar.setter
    def spar(self, spar):
        """Sets the spar of this CalculationStatus.

        List of statuses for SPAR calculation units.  # noqa: E501

        :param spar: The spar of this CalculationStatus.  # noqa: E501
        :type: dict(str, CalculationUnitStatus)
        """

        self._spar = spar

    @property
    def vault(self):
        """Gets the vault of this CalculationStatus.  # noqa: E501

        List of statuses for Vault calculation units.  # noqa: E501

        :return: The vault of this CalculationStatus.  # noqa: E501
        :rtype: dict(str, CalculationUnitStatus)
        """
        return self._vault

    @vault.setter
    def vault(self, vault):
        """Sets the vault of this CalculationStatus.

        List of statuses for Vault calculation units.  # noqa: E501

        :param vault: The vault of this CalculationStatus.  # noqa: E501
        :type: dict(str, CalculationUnitStatus)
        """

        self._vault = vault

    @property
    def pub(self):
        """Gets the pub of this CalculationStatus.  # noqa: E501

        List of statuses for Publisher calculation units.  # noqa: E501

        :return: The pub of this CalculationStatus.  # noqa: E501
        :rtype: dict(str, CalculationUnitStatus)
        """
        return self._pub

    @pub.setter
    def pub(self, pub):
        """Sets the pub of this CalculationStatus.

        List of statuses for Publisher calculation units.  # noqa: E501

        :param pub: The pub of this CalculationStatus.  # noqa: E501
        :type: dict(str, CalculationUnitStatus)
        """

        self._pub = pub

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
        if not isinstance(other, CalculationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CalculationStatus):
            return True

        return self.to_dict() != other.to_dict()
