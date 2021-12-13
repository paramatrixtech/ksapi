# coding: utf-8


import pprint
import re  # noqa: F401

import six

from ks_api_client.configuration import Configuration


class NewSOROrder(object):
    

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'instrumentToken': 'int',
        'transactionType': 'str',
        'quantity': 'int',
        'price': 'float',
        'validity': 'str',
        'variety': 'str',
        'disclosedQuantity': 'int',
        'triggerPrice': 'float',
        'tag': 'str'
    }

    attribute_map = {
        'instrumentToken': 'instrumentToken',
        'transactionType': 'transactionType',
        'quantity': 'quantity',
        'price': 'price',
        'validity': 'validity',
        'variety': 'variety',
        'disclosedQuantity': 'disclosedQuantity',
        'triggerPrice': 'triggerPrice',
        'tag': 'tag'
    }

    def __init__(self, instrumentToken=None, transactionType=None, quantity=None, price=None, validity=None, variety=None, disclosedQuantity=None, triggerPrice=None, tag=None, local_vars_configuration=None):  # noqa: E501
        """NewSOROrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instrumentToken = None
        self._transactionType = None
        self._quantity = None
        self._price = None
        self._validity = None
        self._variety = None
        self._disclosedQuantity = None
        self._triggerPrice = None
        self._tag = None
        self.discriminator = None

        if instrumentToken is not None:
            self.instrumentToken = instrumentToken
        if transactionType is not None:
            self.transactionType = transactionType
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price
        if validity is not None:
            self.validity = validity
        if variety is not None:
            self.variety = variety
        if disclosedQuantity is not None:
            self.disclosedQuantity = disclosedQuantity
        if triggerPrice is not None:
            self.triggerPrice = triggerPrice
        if tag is not None:
            self.tag = tag

    @property
    def instrumentToken(self):
        """Gets the instrumentToken of this NewSOROrder.  # noqa: E501

        Instrument token of the scrip to be traded.<br> Instrument tokens can be found at the following urls (NOTE: Please replace DD_MM_YYYY with the latest date for updated instrument tokens, for example 27_05_2021 will give tokens for 27 may):<br> Equity: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_Cash_DD_MM_YYYY.txt <br> Derivatives: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_FNO_DD_MM_YYYY.txt  # noqa: E501

        :return: The instrumentToken of this NewSOROrder.  # noqa: E501
        :rtype: int
        """
        return self._instrumentToken

    @instrumentToken.setter
    def instrumentToken(self, instrumentToken):
        """Sets the instrumentToken of this NewSOROrder.

        Instrument token of the scrip to be traded.<br> Instrument tokens can be found at the following urls (NOTE: Please replace DD_MM_YYYY with the latest date for updated instrument tokens, for example 27_05_2021 will give tokens for 27 may):<br> Equity: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_Cash_DD_MM_YYYY.txt <br> Derivatives: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_FNO_DD_MM_YYYY.txt  # noqa: E501

        :param instrumentToken: The instrumentToken of this NewSOROrder.  # noqa: E501
        :type instrumentToken: int
        """

        self._instrumentToken = instrumentToken

    @property
    def transactionType(self):
        """Gets the transactionType of this NewSOROrder.  # noqa: E501

        Transaction Type - BUY or SELL  # noqa: E501

        :return: The transactionType of this NewSOROrder.  # noqa: E501
        :rtype: str
        """
        return self._transactionType

    @transactionType.setter
    def transactionType(self, transactionType):
        """Sets the transactionType of this NewSOROrder.

        Transaction Type - BUY or SELL  # noqa: E501

        :param transactionType: The transactionType of this NewSOROrder.  # noqa: E501
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
    def quantity(self):
        """Gets the quantity of this NewSOROrder.  # noqa: E501

        Order quantity - specified in same unit as quoted in market depth  # noqa: E501

        :return: The quantity of this NewSOROrder.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this NewSOROrder.

        Order quantity - specified in same unit as quoted in market depth  # noqa: E501

        :param quantity: The quantity of this NewSOROrder.  # noqa: E501
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def price(self):
        """Gets the price of this NewSOROrder.  # noqa: E501

        Order Price for SOR order is always zero i.e. Market Order  # noqa: E501

        :return: The price of this NewSOROrder.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this NewSOROrder.

        Order Price for SOR order is always zero i.e. Market Order  # noqa: E501

        :param price: The price of this NewSOROrder.  # noqa: E501
        :type price: float
        """

        self._price = price

    @property
    def validity(self):
        """Gets the validity of this NewSOROrder.  # noqa: E501

        Validity of the order - GFD for SOR by default  # noqa: E501

        :return: The validity of this NewSOROrder.  # noqa: E501
        :rtype: str
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this NewSOROrder.

        Validity of the order - GFD for SOR by default  # noqa: E501

        :param validity: The validity of this NewSOROrder.  # noqa: E501
        :type validity: str
        """
        allowed_values = ["GFD"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and validity not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `validity` ({0}), must be one of {1}"  # noqa: E501
                .format(validity, allowed_values)
            )

        self._validity = validity

    @property
    def variety(self):
        """Gets the variety of this NewSOROrder.  # noqa: E501

        Variety of the SOR order - REGULAR by Default.  # noqa: E501

        :return: The variety of this NewSOROrder.  # noqa: E501
        :rtype: str
        """
        return self._variety

    @variety.setter
    def variety(self, variety):
        """Sets the variety of this NewSOROrder.

        Variety of the SOR order - REGULAR by Default.  # noqa: E501

        :param variety: The variety of this NewSOROrder.  # noqa: E501
        :type variety: str
        """
        allowed_values = ["REGULAR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and variety not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `variety` ({0}), must be one of {1}"  # noqa: E501
                .format(variety, allowed_values)
            )

        self._variety = variety

    @property
    def disclosedQuantity(self):
        """Gets the disclosedQuantity of this NewSOROrder.  # noqa: E501

        Quantity to be disclosed in order  # noqa: E501

        :return: The disclosedQuantity of this NewSOROrder.  # noqa: E501
        :rtype: int
        """
        return self._disclosedQuantity

    @disclosedQuantity.setter
    def disclosedQuantity(self, disclosedQuantity):
        """Sets the disclosedQuantity of this NewSOROrder.

        Quantity to be disclosed in order  # noqa: E501

        :param disclosedQuantity: The disclosedQuantity of this NewSOROrder.  # noqa: E501
        :type disclosedQuantity: int
        """

        self._disclosedQuantity = disclosedQuantity

    @property
    def triggerPrice(self):
        """Gets the triggerPrice of this NewSOROrder.  # noqa: E501

        Trigger price, required for stoploss or supermultiple order  # noqa: E501

        :return: The triggerPrice of this NewSOROrder.  # noqa: E501
        :rtype: float
        """
        return self._triggerPrice

    @triggerPrice.setter
    def triggerPrice(self, triggerPrice):
        """Sets the triggerPrice of this NewSOROrder.

        Trigger price, required for stoploss or supermultiple order  # noqa: E501

        :param triggerPrice: The triggerPrice of this NewSOROrder.  # noqa: E501
        :type triggerPrice: float
        """

        self._triggerPrice = triggerPrice

    @property
    def tag(self):
        """Gets the tag of this NewSOROrder.  # noqa: E501

        Tag for this order  # noqa: E501

        :return: The tag of this NewSOROrder.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this NewSOROrder.

        Tag for this order  # noqa: E501

        :param tag: The tag of this NewSOROrder.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

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
        if not isinstance(other, NewSOROrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewSOROrder):
            return True

        return self.to_dict() != other.to_dict()
