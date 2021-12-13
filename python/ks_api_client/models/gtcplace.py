# coding: utf-8


import pprint
import re  # noqa: F401

import six

from ks_api_client.configuration import Configuration


class Gtcplace(object):
    

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'closeDate': 'str'
    }

    attribute_map = {
        'closeDate': 'closeDate'
    }

    def __init__(self, closeDate=None, local_vars_configuration=None):  # noqa: E501
        """Gtcplace - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._closeDate = None
        self.discriminator = None

        if closeDate is not None:
            self.closeDate = closeDate

    @property
    def closeDate(self):
        """Gets the closeDate of this Gtcplace.  # noqa: E501

        Close date for GTC order till which order to be placed in exchange by system.  # noqa: E501

        :return: The closeDate of this Gtcplace.  # noqa: E501
        :rtype: str
        """
        return self._closeDate

    @closeDate.setter
    def closeDate(self, closeDate):
        """Sets the closeDate of this Gtcplace.

        Close date for GTC order till which order to be placed in exchange by system.  # noqa: E501

        :param closeDate: The closeDate of this Gtcplace.  # noqa: E501
        :type closeDate: str
        """

        self._closeDate = closeDate

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
        if not isinstance(other, Gtcplace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Gtcplace):
            return True

        return self.to_dict() != other.to_dict()
