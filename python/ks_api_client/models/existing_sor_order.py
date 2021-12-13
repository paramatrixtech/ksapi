# coding: utf-8


import pprint
import re  # noqa: F401

import six

from ks_api_client.configuration import Configuration


class ExistingSOROrder(object):
    

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'orderId': 'str',
        'quantity': 'int',
        'price': 'float',
        'disclosedQuantity': 'int',
        'triggerPrice': 'float',
        'validity': 'str'
    }

    attribute_map = {
        'orderId': 'orderId',
        'quantity': 'quantity',
        'price': 'price',
        'disclosedQuantity': 'disclosedQuantity',
        'triggerPrice': 'triggerPrice',
        'validity': 'validity'
    }

    def __init__(self, orderId=None, quantity=None, price=None, disclosedQuantity=None, triggerPrice=None, validity=None, local_vars_configuration=None):  # noqa: E501
        """ExistingSOROrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._orderId = None
        self._quantity = None
        self._price = None
        self._disclosedQuantity = None
        self._triggerPrice = None
        self._validity = None
        self.discriminator = None

        self.orderId = orderId
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price
        if disclosedQuantity is not None:
            self.disclosedQuantity = disclosedQuantity
        if triggerPrice is not None:
            self.triggerPrice = triggerPrice
        if validity is not None:
            self.validity = validity

    @property
    def orderId(self):
        """Gets the orderId of this ExistingSOROrder.  # noqa: E501

        Order ID of the order to be modified  # noqa: E501

        :return: The orderId of this ExistingSOROrder.  # noqa: E501
        :rtype: str
        """
        return self._orderId

    @orderId.setter
    def orderId(self, orderId):
        """Sets the orderId of this ExistingSOROrder.

        Order ID of the order to be modified  # noqa: E501

        :param orderId: The orderId of this ExistingSOROrder.  # noqa: E501
        :type orderId: str
        """
        if self.local_vars_configuration.client_side_validation and orderId is None:  # noqa: E501
            raise ValueError("Invalid value for `orderId`, must not be `None`")  # noqa: E501

        self._orderId = orderId

    @property
    def quantity(self):
        """Gets the quantity of this ExistingSOROrder.  # noqa: E501

        Order quantity - specified in same unit as quoted in market depth  # noqa: E501

        :return: The quantity of this ExistingSOROrder.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ExistingSOROrder.

        Order quantity - specified in same unit as quoted in market depth  # noqa: E501

        :param quantity: The quantity of this ExistingSOROrder.  # noqa: E501
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def price(self):
        """Gets the price of this ExistingSOROrder.  # noqa: E501

        Order Price, non zero positive for limit order and zero for market order  # noqa: E501

        :return: The price of this ExistingSOROrder.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ExistingSOROrder.

        Order Price, non zero positive for limit order and zero for market order  # noqa: E501

        :param price: The price of this ExistingSOROrder.  # noqa: E501
        :type price: float
        """

        self._price = price

    @property
    def disclosedQuantity(self):
        """Gets the disclosedQuantity of this ExistingSOROrder.  # noqa: E501

        Quantity to be disclosed in order  # noqa: E501

        :return: The disclosedQuantity of this ExistingSOROrder.  # noqa: E501
        :rtype: int
        """
        return self._disclosedQuantity

    @disclosedQuantity.setter
    def disclosedQuantity(self, disclosedQuantity):
        """Sets the disclosedQuantity of this ExistingSOROrder.

        Quantity to be disclosed in order  # noqa: E501

        :param disclosedQuantity: The disclosedQuantity of this ExistingSOROrder.  # noqa: E501
        :type disclosedQuantity: int
        """

        self._disclosedQuantity = disclosedQuantity

    @property
    def triggerPrice(self):
        """Gets the triggerPrice of this ExistingSOROrder.  # noqa: E501

        Trigger price, required for stoploss or supermultiple order  # noqa: E501

        :return: The triggerPrice of this ExistingSOROrder.  # noqa: E501
        :rtype: float
        """
        return self._triggerPrice

    @triggerPrice.setter
    def triggerPrice(self, triggerPrice):
        """Sets the triggerPrice of this ExistingSOROrder.

        Trigger price, required for stoploss or supermultiple order  # noqa: E501

        :param triggerPrice: The triggerPrice of this ExistingSOROrder.  # noqa: E501
        :type triggerPrice: float
        """

        self._triggerPrice = triggerPrice

    @property
    def validity(self):
        """Gets the validity of this ExistingSOROrder.  # noqa: E501

        Validity of the order - GFD for SOR by default  # noqa: E501

        :return: The validity of this ExistingSOROrder.  # noqa: E501
        :rtype: str
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this ExistingSOROrder.

        Validity of the order - GFD for SOR by default  # noqa: E501

        :param validity: The validity of this ExistingSOROrder.  # noqa: E501
        :type validity: str
        """
        allowed_values = ["GFD"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and validity not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `validity` ({0}), must be one of {1}"  # noqa: E501
                .format(validity, allowed_values)
            )

        self._validity = validity

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
        if not isinstance(other, ExistingSOROrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExistingSOROrder):
            return True

        return self.to_dict() != other.to_dict()
