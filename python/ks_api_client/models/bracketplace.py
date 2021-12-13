# coding: utf-8


import pprint
import re  # noqa: F401

import six

from ks_api_client.configuration import Configuration


class Bracketplace(object):
    

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'Spread': 'float',
        'trailingPrice': 'float',
        'bookProfit': 'float',
        'bookDisclosedQty': 'int'
    }

    attribute_map = {
        'Spread': 'Spread',
        'trailingPrice': 'trailingPrice',
        'bookProfit': 'bookProfit',
        'bookDisclosedQty': 'bookDisclosedQty'
    }

    def __init__(self, Spread=None, trailingPrice=None, bookProfit=None, bookDisclosedQty=None, local_vars_configuration=None):  # noqa: E501
        """Bracketplace - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._Spread = None
        self._trailingPrice = None
        self._bookProfit = None
        self._bookDisclosedQty = None
        self.discriminator = None

        if Spread is not None:
            self.Spread = Spread
        if trailingPrice is not None:
            self.trailingPrice = trailingPrice
        if bookProfit is not None:
            self.bookProfit = bookProfit
        if bookDisclosedQty is not None:
            self.bookDisclosedQty = bookDisclosedQty

    @property
    def Spread(self):
        """Gets the Spread of this Bracketplace.  # noqa: E501

        Spread of the order  # noqa: E501

        :return: The Spread of this Bracketplace.  # noqa: E501
        :rtype: float
        """
        return self._Spread

    @Spread.setter
    def Spread(self, Spread):
        """Sets the Spread of this Bracketplace.

        Spread of the order  # noqa: E501

        :param Spread: The Spread of this Bracketplace.  # noqa: E501
        :type Spread: float
        """

        self._Spread = Spread

    @property
    def trailingPrice(self):
        """Gets the trailingPrice of this Bracketplace.  # noqa: E501

        Triling price of TSLO Order.  # noqa: E501

        :return: The trailingPrice of this Bracketplace.  # noqa: E501
        :rtype: float
        """
        return self._trailingPrice

    @trailingPrice.setter
    def trailingPrice(self, trailingPrice):
        """Sets the trailingPrice of this Bracketplace.

        Triling price of TSLO Order.  # noqa: E501

        :param trailingPrice: The trailingPrice of this Bracketplace.  # noqa: E501
        :type trailingPrice: float
        """

        self._trailingPrice = trailingPrice

    @property
    def bookProfit(self):
        """Gets the bookProfit of this Bracketplace.  # noqa: E501

        Book Profit Price of the order  # noqa: E501

        :return: The bookProfit of this Bracketplace.  # noqa: E501
        :rtype: float
        """
        return self._bookProfit

    @bookProfit.setter
    def bookProfit(self, bookProfit):
        """Sets the bookProfit of this Bracketplace.

        Book Profit Price of the order  # noqa: E501

        :param bookProfit: The bookProfit of this Bracketplace.  # noqa: E501
        :type bookProfit: float
        """

        self._bookProfit = bookProfit

    @property
    def bookDisclosedQty(self):
        """Gets the bookDisclosedQty of this Bracketplace.  # noqa: E501

        Quantity to be disclosed in bracket order  # noqa: E501

        :return: The bookDisclosedQty of this Bracketplace.  # noqa: E501
        :rtype: int
        """
        return self._bookDisclosedQty

    @bookDisclosedQty.setter
    def bookDisclosedQty(self, bookDisclosedQty):
        """Sets the bookDisclosedQty of this Bracketplace.

        Quantity to be disclosed in bracket order  # noqa: E501

        :param bookDisclosedQty: The bookDisclosedQty of this Bracketplace.  # noqa: E501
        :type bookDisclosedQty: int
        """

        self._bookDisclosedQty = bookDisclosedQty

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
        if not isinstance(other, Bracketplace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Bracketplace):
            return True

        return self.to_dict() != other.to_dict()
