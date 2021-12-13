# coding: utf-8


import pprint
import re  # noqa: F401

import six

from ks_api_client.configuration import Configuration


class Gtcmodify(object):
    

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'gtcOrderNo': 'str'
    }

    attribute_map = {
        'gtcOrderNo': 'gtcOrderNo'
    }

    def __init__(self, gtcOrderNo=None, local_vars_configuration=None):  # noqa: E501
        """Gtcmodify - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gtcOrderNo = None
        self.discriminator = None

        if gtcOrderNo is not None:
            self.gtcOrderNo = gtcOrderNo

    @property
    def gtcOrderNo(self):
        """Gets the gtcOrderNo of this Gtcmodify.  # noqa: E501

        Order Number to modify  # noqa: E501

        :return: The gtcOrderNo of this Gtcmodify.  # noqa: E501
        :rtype: str
        """
        return self._gtcOrderNo

    @gtcOrderNo.setter
    def gtcOrderNo(self, gtcOrderNo):
        """Sets the gtcOrderNo of this Gtcmodify.

        Order Number to modify  # noqa: E501

        :param gtcOrderNo: The gtcOrderNo of this Gtcmodify.  # noqa: E501
        :type gtcOrderNo: str
        """

        self._gtcOrderNo = gtcOrderNo

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
        if not isinstance(other, Gtcmodify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Gtcmodify):
            return True

        return self.to_dict() != other.to_dict()
