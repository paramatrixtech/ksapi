# coding: utf-8


import pprint
import re  # noqa: F401

import six

from ks_api_client.configuration import Configuration


class Codplace(object):
    

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'squareOffFlag': 'int'
    }

    attribute_map = {
        'squareOffFlag': 'squareOffFlag'
    }

    def __init__(self, squareOffFlag=None, local_vars_configuration=None):  # noqa: E501
        """Codplace - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._squareOffFlag = None
        self.discriminator = None

        if squareOffFlag is not None:
            self.squareOffFlag = squareOffFlag

    @property
    def squareOffFlag(self):
        """Gets the squareOffFlag of this Codplace.  # noqa: E501

        Square off flag for COD order, 1 to auto square off order. 0 - for no auto Square off by system.  # noqa: E501

        :return: The squareOffFlag of this Codplace.  # noqa: E501
        :rtype: int
        """
        return self._squareOffFlag

    @squareOffFlag.setter
    def squareOffFlag(self, squareOffFlag):
        """Sets the squareOffFlag of this Codplace.

        Square off flag for COD order, 1 to auto square off order. 0 - for no auto Square off by system.  # noqa: E501

        :param squareOffFlag: The squareOffFlag of this Codplace.  # noqa: E501
        :type squareOffFlag: int
        """

        self._squareOffFlag = squareOffFlag

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
        if not isinstance(other, Codplace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Codplace):
            return True

        return self.to_dict() != other.to_dict()
