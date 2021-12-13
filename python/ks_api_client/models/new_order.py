# coding: utf-8


import pprint
import re  # noqa: F401

import six

from ks_api_client.configuration import Configuration


class NewOrder(object):
    

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
        'product': 'str',
        'validity': 'str',
        'variety': 'str',
        'disclosedQuantity': 'int',
        'triggerPrice': 'float',
        'tslo': 'Tsloplace',
        'bracket': 'Bracketplace',
        'tslonew': 'Tsloplace',
        'bracketnew': 'Bracketplace',
        'gtc': 'Gtcplace',
        'ctd': 'Ctdplace',
        'cod': 'Codplace',
        'tag': 'str',
        'smartOrderRouting': 'str'
    }

    attribute_map = {
        'instrumentToken': 'instrumentToken',
        'transactionType': 'transactionType',
        'quantity': 'quantity',
        'price': 'price',
        'product': 'product',
        'validity': 'validity',
        'variety': 'variety',
        'disclosedQuantity': 'disclosedQuantity',
        'triggerPrice': 'triggerPrice',
        'tslo': 'tslo',
        'bracket': 'bracket',
        'tslonew': 'tslonew',
        'bracketnew': 'bracketnew',
        'gtc': 'gtc',
        'ctd': 'ctd',
        'cod': 'cod',
        'tag': 'tag',
        'smartOrderRouting': 'smartOrderRouting'
    }

    def __init__(self, instrumentToken=None, transactionType=None, quantity=None, price=None, product=None, validity=None, variety=None, disclosedQuantity=None, triggerPrice=None, tslo=None, bracket=None, tslonew=None, bracketnew=None, gtc=None, ctd=None, cod=None, tag=None, smartOrderRouting=None, local_vars_configuration=None):  # noqa: E501
        """NewOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instrumentToken = None
        self._transactionType = None
        self._quantity = None
        self._price = None
        self._product = None
        self._validity = None
        self._variety = None
        self._disclosedQuantity = None
        self._triggerPrice = None
        self._tslo = None
        self._bracket = None
        self._tslonew = None
        self._bracketnew = None
        self._gtc = None
        self._ctd = None
        self._cod = None
        self._tag = None
        self._smartOrderRouting = None
        self.discriminator = None

        if instrumentToken is not None:
            self.instrumentToken = instrumentToken
        if transactionType is not None:
            self.transactionType = transactionType
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price
        if product is not None:
            self.product = product
        if validity is not None:
            self.validity = validity
        if variety is not None:
            self.variety = variety
        if disclosedQuantity is not None:
            self.disclosedQuantity = disclosedQuantity
        if triggerPrice is not None:
            self.triggerPrice = triggerPrice
        if tslo is not None:
            self.tslo = tslo
        if bracket is not None:
            self.bracket = bracket
        if tslonew is not None:
            self.tslonew = tslonew
        if bracketnew is not None:
            self.bracketnew = bracketnew
        if gtc is not None:
            self.gtc = gtc
        if ctd is not None:
            self.ctd = ctd
        if cod is not None:
            self.cod = cod
        if tag is not None:
            self.tag = tag
        if smartOrderRouting is not None:
            self.smartOrderRouting = smartOrderRouting

    @property
    def instrumentToken(self):
        """Gets the instrumentToken of this NewOrder.  # noqa: E501

        Instrument token of the scrip to be traded.<br> Instrument tokens can be found at the following urls (NOTE: Please replace DD_MM_YYYY with the latest date for updated instrument tokens, for example 27_05_2021 will give tokens for 27 may):<br> Equity: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_Cash_DD_MM_YYYY.txt <br> Derivatives: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_FNO_DD_MM_YYYY.txt.  # noqa: E501

        :return: The instrumentToken of this NewOrder.  # noqa: E501
        :rtype: int
        """
        return self._instrumentToken

    @instrumentToken.setter
    def instrumentToken(self, instrumentToken):
        """Sets the instrumentToken of this NewOrder.

        Instrument token of the scrip to be traded.<br> Instrument tokens can be found at the following urls (NOTE: Please replace DD_MM_YYYY with the latest date for updated instrument tokens, for example 27_05_2021 will give tokens for 27 may):<br> Equity: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_Cash_DD_MM_YYYY.txt <br> Derivatives: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_FNO_DD_MM_YYYY.txt.  # noqa: E501

        :param instrumentToken: The instrumentToken of this NewOrder.  # noqa: E501
        :type instrumentToken: int
        """

        self._instrumentToken = instrumentToken

    @property
    def transactionType(self):
        """Gets the transactionType of this NewOrder.  # noqa: E501

        Transaction Type - BUY or SELL  # noqa: E501

        :return: The transactionType of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._transactionType

    @transactionType.setter
    def transactionType(self, transactionType):
        """Sets the transactionType of this NewOrder.

        Transaction Type - BUY or SELL  # noqa: E501

        :param transactionType: The transactionType of this NewOrder.  # noqa: E501
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
        """Gets the quantity of this NewOrder.  # noqa: E501

        Order quantity - specified in same unit as quoted in market depth  # noqa: E501

        :return: The quantity of this NewOrder.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this NewOrder.

        Order quantity - specified in same unit as quoted in market depth  # noqa: E501

        :param quantity: The quantity of this NewOrder.  # noqa: E501
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def price(self):
        """Gets the price of this NewOrder.  # noqa: E501

        Order Price, non zero positive for limit order and zero for market order  # noqa: E501

        :return: The price of this NewOrder.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this NewOrder.

        Order Price, non zero positive for limit order and zero for market order  # noqa: E501

        :param price: The price of this NewOrder.  # noqa: E501
        :type price: float
        """

        self._price = price

    @property
    def product(self):
        """Gets the product of this NewOrder.  # noqa: E501

        Product type for this order - NORMAL, SUPERMULTIPLE, SUPERMULTIPLEOPTION, MTF  # noqa: E501

        :return: The product of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this NewOrder.

        Product type for this order - NORMAL, SUPERMULTIPLE, SUPERMULTIPLEOPTION, MTF  # noqa: E501

        :param product: The product of this NewOrder.  # noqa: E501
        :type product: str
        """
        allowed_values = ["NORMAL", "SUPERMULTIPLE", "SUPERMULTIPLEOPTION", "MTF", "SOR", "TSLONEW", "BRACKETNEW", "TSLO", "BRACKET", "GTC", "COD", "CONVERT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and product not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `product` ({0}), must be one of {1}"  # noqa: E501
                .format(product, allowed_values)
            )

        self._product = product

    @property
    def validity(self):
        """Gets the validity of this NewOrder.  # noqa: E501

        Validity of the order - GFD, IOC etc  # noqa: E501

        :return: The validity of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this NewOrder.

        Validity of the order - GFD, IOC etc  # noqa: E501

        :param validity: The validity of this NewOrder.  # noqa: E501
        :type validity: str
        """
        allowed_values = ["GFD", "IOC"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and validity not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `validity` ({0}), must be one of {1}"  # noqa: E501
                .format(validity, allowed_values)
            )

        self._validity = validity

    @property
    def variety(self):
        """Gets the variety of this NewOrder.  # noqa: E501

        Variety of the order - REGULAR, AMO, SQUAREOFF - for Super Multiple Orders etc  # noqa: E501

        :return: The variety of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._variety

    @variety.setter
    def variety(self, variety):
        """Sets the variety of this NewOrder.

        Variety of the order - REGULAR, AMO, SQUAREOFF - for Super Multiple Orders etc  # noqa: E501

        :param variety: The variety of this NewOrder.  # noqa: E501
        :type variety: str
        """
        allowed_values = ["REGULAR", "AMO", "SQUAREOFF"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and variety not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `variety` ({0}), must be one of {1}"  # noqa: E501
                .format(variety, allowed_values)
            )

        self._variety = variety

    @property
    def disclosedQuantity(self):
        """Gets the disclosedQuantity of this NewOrder.  # noqa: E501

        Quantity to be disclosed in order  # noqa: E501

        :return: The disclosedQuantity of this NewOrder.  # noqa: E501
        :rtype: int
        """
        return self._disclosedQuantity

    @disclosedQuantity.setter
    def disclosedQuantity(self, disclosedQuantity):
        """Sets the disclosedQuantity of this NewOrder.

        Quantity to be disclosed in order  # noqa: E501

        :param disclosedQuantity: The disclosedQuantity of this NewOrder.  # noqa: E501
        :type disclosedQuantity: int
        """

        self._disclosedQuantity = disclosedQuantity

    @property
    def triggerPrice(self):
        """Gets the triggerPrice of this NewOrder.  # noqa: E501

        Trigger price, required for stoploss or supermultiple order  # noqa: E501

        :return: The triggerPrice of this NewOrder.  # noqa: E501
        :rtype: float
        """
        return self._triggerPrice

    @triggerPrice.setter
    def triggerPrice(self, triggerPrice):
        """Sets the triggerPrice of this NewOrder.

        Trigger price, required for stoploss or supermultiple order  # noqa: E501

        :param triggerPrice: The triggerPrice of this NewOrder.  # noqa: E501
        :type triggerPrice: float
        """

        self._triggerPrice = triggerPrice

    @property
    def tslo(self):
        """Gets the tslo of this NewOrder.  # noqa: E501


        :return: The tslo of this NewOrder.  # noqa: E501
        :rtype: Tsloplace
        """
        return self._tslo

    @tslo.setter
    def tslo(self, tslo):
        """Sets the tslo of this NewOrder.


        :param tslo: The tslo of this NewOrder.  # noqa: E501
        :type tslo: Tsloplace
        """

        self._tslo = tslo

    @property
    def bracket(self):
        """Gets the bracket of this NewOrder.  # noqa: E501


        :return: The bracket of this NewOrder.  # noqa: E501
        :rtype: Bracketplace
        """
        return self._bracket

    @bracket.setter
    def bracket(self, bracket):
        """Sets the bracket of this NewOrder.


        :param bracket: The bracket of this NewOrder.  # noqa: E501
        :type bracket: Bracketplace
        """

        self._bracket = bracket

    @property
    def tslonew(self):
        """Gets the tslonew of this NewOrder.  # noqa: E501


        :return: The tslonew of this NewOrder.  # noqa: E501
        :rtype: Tsloplace
        """
        return self._tslonew

    @tslonew.setter
    def tslonew(self, tslonew):
        """Sets the tslonew of this NewOrder.


        :param tslonew: The tslonew of this NewOrder.  # noqa: E501
        :type tslonew: Tsloplace
        """

        self._tslonew = tslonew

    @property
    def bracketnew(self):
        """Gets the bracketnew of this NewOrder.  # noqa: E501


        :return: The bracketnew of this NewOrder.  # noqa: E501
        :rtype: Bracketplace
        """
        return self._bracketnew

    @bracketnew.setter
    def bracketnew(self, bracketnew):
        """Sets the bracketnew of this NewOrder.


        :param bracketnew: The bracketnew of this NewOrder.  # noqa: E501
        :type bracketnew: Bracketplace
        """

        self._bracketnew = bracketnew

    @property
    def gtc(self):
        """Gets the gtc of this NewOrder.  # noqa: E501


        :return: The gtc of this NewOrder.  # noqa: E501
        :rtype: Gtcplace
        """
        return self._gtc

    @gtc.setter
    def gtc(self, gtc):
        """Sets the gtc of this NewOrder.


        :param gtc: The gtc of this NewOrder.  # noqa: E501
        :type gtc: Gtcplace
        """

        self._gtc = gtc

    @property
    def ctd(self):
        """Gets the ctd of this NewOrder.  # noqa: E501


        :return: The ctd of this NewOrder.  # noqa: E501
        :rtype: Ctdplace
        """
        return self._ctd

    @ctd.setter
    def ctd(self, ctd):
        """Sets the ctd of this NewOrder.


        :param ctd: The ctd of this NewOrder.  # noqa: E501
        :type ctd: Ctdplace
        """

        self._ctd = ctd

    @property
    def cod(self):
        """Gets the cod of this NewOrder.  # noqa: E501


        :return: The cod of this NewOrder.  # noqa: E501
        :rtype: Codplace
        """
        return self._cod

    @cod.setter
    def cod(self, cod):
        """Sets the cod of this NewOrder.


        :param cod: The cod of this NewOrder.  # noqa: E501
        :type cod: Codplace
        """

        self._cod = cod

    @property
    def tag(self):
        """Gets the tag of this NewOrder.  # noqa: E501

        Tag for this order  # noqa: E501

        :return: The tag of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this NewOrder.

        Tag for this order  # noqa: E501

        :param tag: The tag of this NewOrder.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

    @property
    def smartOrderRouting(self):
        """Gets the smartOrderRouting of this NewOrder.  # noqa: E501

        smart Order Routing for this order  # noqa: E501

        :return: The smartOrderRouting of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._smartOrderRouting

    @smartOrderRouting.setter
    def smartOrderRouting(self, smartOrderRouting):
        """Sets the smartOrderRouting of this NewOrder.

        smart Order Routing for this order  # noqa: E501

        :param smartOrderRouting: The smartOrderRouting of this NewOrder.  # noqa: E501
        :type smartOrderRouting: str
        """

        self._smartOrderRouting = smartOrderRouting

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
        if not isinstance(other, NewOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewOrder):
            return True

        return self.to_dict() != other.to_dict()
