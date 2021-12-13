# coding: utf-8


import pprint
import re  # noqa: F401

import six

from ks_api_client.configuration import Configuration


class OrderInfo(object):
    

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'instrumentToken': 'int',
        'quantity': 'int',
        'price': 'float',
        'amount': 'int',
        'triggerPrice': 'float'
    }

    attribute_map = {
        'instrumentToken': 'instrumentToken',
        'quantity': 'quantity',
        'price': 'price',
        'amount': 'amount',
        'triggerPrice': 'triggerPrice'
    }

    def __init__(self, instrumentToken=None, quantity=None, price=None, amount=None, triggerPrice=None, local_vars_configuration=None):  # noqa: E501
        """OrderInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instrumentToken = None
        self._quantity = None
        self._price = None
        self._amount = None
        self._triggerPrice = None
        self.discriminator = None

        if instrumentToken is not None:
            self.instrumentToken = instrumentToken
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price
        if amount is not None:
            self.amount = amount
        if triggerPrice is not None:
            self.triggerPrice = triggerPrice

    @property
    def instrumentToken(self):
        """Gets the instrumentToken of this OrderInfo.  # noqa: E501

        Instrument token of the scrip to be traded.<br> Instrument tokens can be found at the following urls (NOTE: Please replace DD_MM_YYYY with the latest date for updated instrument tokens, for example 27_05_2021 will give tokens for 27 may):<br> Equity: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_Cash_DD_MM_YYYY.txt <br> Derivatives: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_FNO_DD_MM_YYYY.txt  # noqa: E501

        :return: The instrumentToken of this OrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._instrumentToken

    @instrumentToken.setter
    def instrumentToken(self, instrumentToken):
        """Sets the instrumentToken of this OrderInfo.

        Instrument token of the scrip to be traded.<br> Instrument tokens can be found at the following urls (NOTE: Please replace DD_MM_YYYY with the latest date for updated instrument tokens, for example 27_05_2021 will give tokens for 27 may):<br> Equity: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_Cash_DD_MM_YYYY.txt <br> Derivatives: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_FNO_DD_MM_YYYY.txt  # noqa: E501

        :param instrumentToken: The instrumentToken of this OrderInfo.  # noqa: E501
        :type instrumentToken: int
        """

        self._instrumentToken = instrumentToken

    @property
    def quantity(self):
        """Gets the quantity of this OrderInfo.  # noqa: E501

        Order quantity - specified in same unit as quoted in market depth  # noqa: E501

        :return: The quantity of this OrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderInfo.

        Order quantity - specified in same unit as quoted in market depth  # noqa: E501

        :param quantity: The quantity of this OrderInfo.  # noqa: E501
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def price(self):
        """Gets the price of this OrderInfo.  # noqa: E501

        Order Price, non zero positive for limit order and zero for market order  # noqa: E501

        :return: The price of this OrderInfo.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderInfo.

        Order Price, non zero positive for limit order and zero for market order  # noqa: E501

        :param price: The price of this OrderInfo.  # noqa: E501
        :type price: float
        """

        self._price = price

    @property
    def amount(self):
        """Gets the amount of this OrderInfo.  # noqa: E501

        Order Amount  # noqa: E501

        :return: The amount of this OrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this OrderInfo.

        Order Amount  # noqa: E501

        :param amount: The amount of this OrderInfo.  # noqa: E501
        :type amount: int
        """

        self._amount = amount

    @property
    def triggerPrice(self):
        """Gets the triggerPrice of this OrderInfo.  # noqa: E501

        Trigger price, required for stoploss or supermultiple order  # noqa: E501

        :return: The triggerPrice of this OrderInfo.  # noqa: E501
        :rtype: float
        """
        return self._triggerPrice

    @triggerPrice.setter
    def triggerPrice(self, triggerPrice):
        """Sets the triggerPrice of this OrderInfo.

        Trigger price, required for stoploss or supermultiple order  # noqa: E501

        :param triggerPrice: The triggerPrice of this OrderInfo.  # noqa: E501
        :type triggerPrice: float
        """

        self._triggerPrice = triggerPrice

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
        if not isinstance(other, OrderInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderInfo):
            return True

        return self.to_dict() != other.to_dict()
