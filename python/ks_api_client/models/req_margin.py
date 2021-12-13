# coding: utf-8


import pprint
import re  # noqa: F401

import six

from ks_api_client.configuration import Configuration


class ReqMargin(object):
    

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'transactionType': 'str',
        'orderInfo': 'list[OrderInfo]'
    }

    attribute_map = {
        'transactionType': 'transactionType',
        'orderInfo': 'orderInfo'
    }

    def __init__(self, transactionType=None, orderInfo=None, local_vars_configuration=None):  # noqa: E501
        """ReqMargin - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._transactionType = None
        self._orderInfo = None
        self.discriminator = None

        if transactionType is not None:
            self.transactionType = transactionType
        if orderInfo is not None:
            self.orderInfo = orderInfo

    @property
    def transactionType(self):
        """Gets the transactionType of this ReqMargin.  # noqa: E501

        Transaction Type - BUY or SELL  # noqa: E501

        :return: The transactionType of this ReqMargin.  # noqa: E501
        :rtype: str
        """
        return self._transactionType

    @transactionType.setter
    def transactionType(self, transactionType):
        """Sets the transactionType of this ReqMargin.

        Transaction Type - BUY or SELL  # noqa: E501

        :param transactionType: The transactionType of this ReqMargin.  # noqa: E501
        :type transactionType: str
        """
        allowed_values = ["BUY", "SELL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and transactionType not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `transactionType` ({0}), must be one of {1}"  # noqa: E501
                .format(transactionType, allowed_values)
            )

        self._transactionType = transactionType

    @property
    def orderInfo(self):
        """Gets the orderInfo of this ReqMargin.  # noqa: E501


        :return: The orderInfo of this ReqMargin.  # noqa: E501
        :rtype: list[OrderInfo]
        """
        return self._orderInfo

    @orderInfo.setter
    def orderInfo(self, orderInfo):
        """Sets the orderInfo of this ReqMargin.


        :param orderInfo: The orderInfo of this ReqMargin.  # noqa: E501
        :type orderInfo: list[OrderInfo]
        """

        self._orderInfo = orderInfo

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
        if not isinstance(other, ReqMargin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReqMargin):
            return True

        return self.to_dict() != other.to_dict()
