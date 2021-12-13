# coding: utf-8


import pprint
import re  # noqa: F401

import six

from ks_api_client.configuration import Configuration


class MarginDet(object):
    

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'instrumentToken': 'int',
        'normal': 'float',
        'supermultiple': 'float',
        'mtf': 'float'
    }

    attribute_map = {
        'instrumentToken': 'instrumentToken',
        'normal': 'normal',
        'supermultiple': 'supermultiple',
        'mtf': 'mtf'
    }

    def __init__(self, instrumentToken=None, normal=None, supermultiple=None, mtf=None, local_vars_configuration=None):  # noqa: E501
        """MarginDet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instrumentToken = None
        self._normal = None
        self._supermultiple = None
        self._mtf = None
        self.discriminator = None

        if instrumentToken is not None:
            self.instrumentToken = instrumentToken
        if normal is not None:
            self.normal = normal
        if supermultiple is not None:
            self.supermultiple = supermultiple
        if mtf is not None:
            self.mtf = mtf

    @property
    def instrumentToken(self):
        """Gets the instrumentToken of this MarginDet.  # noqa: E501


        :return: The instrumentToken of this MarginDet.  # noqa: E501
        :rtype: int
        """
        return self._instrumentToken

    @instrumentToken.setter
    def instrumentToken(self, instrumentToken):
        """Sets the instrumentToken of this MarginDet.


        :param instrumentToken: The instrumentToken of this MarginDet.  # noqa: E501
        :type instrumentToken: int
        """

        self._instrumentToken = instrumentToken

    @property
    def normal(self):
        """Gets the normal of this MarginDet.  # noqa: E501

        Order Status  # noqa: E501

        :return: The normal of this MarginDet.  # noqa: E501
        :rtype: float
        """
        return self._normal

    @normal.setter
    def normal(self, normal):
        """Sets the normal of this MarginDet.

        Order Status  # noqa: E501

        :param normal: The normal of this MarginDet.  # noqa: E501
        :type normal: float
        """

        self._normal = normal

    @property
    def supermultiple(self):
        """Gets the supermultiple of this MarginDet.  # noqa: E501

        Order Status  # noqa: E501

        :return: The supermultiple of this MarginDet.  # noqa: E501
        :rtype: float
        """
        return self._supermultiple

    @supermultiple.setter
    def supermultiple(self, supermultiple):
        """Sets the supermultiple of this MarginDet.

        Order Status  # noqa: E501

        :param supermultiple: The supermultiple of this MarginDet.  # noqa: E501
        :type supermultiple: float
        """

        self._supermultiple = supermultiple

    @property
    def mtf(self):
        """Gets the mtf of this MarginDet.  # noqa: E501

        Order Status  # noqa: E501

        :return: The mtf of this MarginDet.  # noqa: E501
        :rtype: float
        """
        return self._mtf

    @mtf.setter
    def mtf(self, mtf):
        """Sets the mtf of this MarginDet.

        Order Status  # noqa: E501

        :param mtf: The mtf of this MarginDet.  # noqa: E501
        :type mtf: float
        """

        self._mtf = mtf

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
        if not isinstance(other, MarginDet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarginDet):
            return True

        return self.to_dict() != other.to_dict()
