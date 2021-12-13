# coding: utf-8


import pprint
import re  # noqa: F401

import six

from ks_api_client.configuration import Configuration


class Orders(object):
    

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'orderId': 'float',
        'variety': 'str',
        'instrumentName': 'str',
        'instrumentToken': 'str',
        'exchange': 'str',
        'orderQuantity': 'int',
        'pendingQuantity': 'int',
        'cancelledQuantity': 'int',
        'filledQuantity': 'int',
        'disclosedQuantity': 'int',
        'triggerPrice': 'int',
        'price': 'float',
        'product': 'str',
        'transactionType': 'str',
        'orderTimestamp': 'str',
        'validity': 'str',
        'statusMessage': 'str',
        'tag': 'str',
        'status': 'str',
        'statusInfo': 'str',
        'isFNO': 'str'
    }

    attribute_map = {
        'orderId': 'orderId',
        'variety': 'variety',
        'instrumentName': 'instrumentName',
        'instrumentToken': 'instrumentToken',
        'exchange': 'exchange',
        'orderQuantity': 'orderQuantity',
        'pendingQuantity': 'pendingQuantity',
        'cancelledQuantity': 'cancelledQuantity',
        'filledQuantity': 'filledQuantity',
        'disclosedQuantity': 'disclosedQuantity',
        'triggerPrice': 'triggerPrice',
        'price': 'price',
        'product': 'product',
        'transactionType': 'transactionType',
        'orderTimestamp': 'orderTimestamp',
        'validity': 'validity',
        'statusMessage': 'statusMessage',
        'tag': 'tag',
        'status': 'status',
        'statusInfo': 'statusInfo',
        'isFNO': 'isFNO'
    }

    def __init__(self, orderId=None, variety=None, instrumentName=None, instrumentToken=None, exchange=None, orderQuantity=None, pendingQuantity=None, cancelledQuantity=None, filledQuantity=None, disclosedQuantity=None, triggerPrice=None, price=None, product=None, transactionType=None, orderTimestamp=None, validity=None, statusMessage=None, tag=None, status=None, statusInfo=None, isFNO=None, local_vars_configuration=None):  # noqa: E501
        """Orders - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._orderId = None
        self._variety = None
        self._instrumentName = None
        self._instrumentToken = None
        self._exchange = None
        self._orderQuantity = None
        self._pendingQuantity = None
        self._cancelledQuantity = None
        self._filledQuantity = None
        self._disclosedQuantity = None
        self._triggerPrice = None
        self._price = None
        self._product = None
        self._transactionType = None
        self._orderTimestamp = None
        self._validity = None
        self._statusMessage = None
        self._tag = None
        self._status = None
        self._statusInfo = None
        self._isFNO = None
        self.discriminator = None

        if orderId is not None:
            self.orderId = orderId
        if variety is not None:
            self.variety = variety
        if instrumentName is not None:
            self.instrumentName = instrumentName
        if instrumentToken is not None:
            self.instrumentToken = instrumentToken
        if exchange is not None:
            self.exchange = exchange
        if orderQuantity is not None:
            self.orderQuantity = orderQuantity
        if pendingQuantity is not None:
            self.pendingQuantity = pendingQuantity
        if cancelledQuantity is not None:
            self.cancelledQuantity = cancelledQuantity
        if filledQuantity is not None:
            self.filledQuantity = filledQuantity
        if disclosedQuantity is not None:
            self.disclosedQuantity = disclosedQuantity
        if triggerPrice is not None:
            self.triggerPrice = triggerPrice
        if price is not None:
            self.price = price
        if product is not None:
            self.product = product
        if transactionType is not None:
            self.transactionType = transactionType
        if orderTimestamp is not None:
            self.orderTimestamp = orderTimestamp
        if validity is not None:
            self.validity = validity
        if statusMessage is not None:
            self.statusMessage = statusMessage
        if tag is not None:
            self.tag = tag
        if status is not None:
            self.status = status
        if statusInfo is not None:
            self.statusInfo = statusInfo
        if isFNO is not None:
            self.isFNO = isFNO

    @property
    def orderId(self):
        """Gets the orderId of this Orders.  # noqa: E501


        :return: The orderId of this Orders.  # noqa: E501
        :rtype: float
        """
        return self._orderId

    @orderId.setter
    def orderId(self, orderId):
        """Sets the orderId of this Orders.


        :param orderId: The orderId of this Orders.  # noqa: E501
        :type orderId: float
        """

        self._orderId = orderId

    @property
    def variety(self):
        """Gets the variety of this Orders.  # noqa: E501


        :return: The variety of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._variety

    @variety.setter
    def variety(self, variety):
        """Sets the variety of this Orders.


        :param variety: The variety of this Orders.  # noqa: E501
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
    def instrumentName(self):
        """Gets the instrumentName of this Orders.  # noqa: E501


        :return: The instrumentName of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._instrumentName

    @instrumentName.setter
    def instrumentName(self, instrumentName):
        """Sets the instrumentName of this Orders.


        :param instrumentName: The instrumentName of this Orders.  # noqa: E501
        :type instrumentName: str
        """

        self._instrumentName = instrumentName

    @property
    def instrumentToken(self):
        """Gets the instrumentToken of this Orders.  # noqa: E501


        :return: The instrumentToken of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._instrumentToken

    @instrumentToken.setter
    def instrumentToken(self, instrumentToken):
        """Sets the instrumentToken of this Orders.


        :param instrumentToken: The instrumentToken of this Orders.  # noqa: E501
        :type instrumentToken: str
        """

        self._instrumentToken = instrumentToken

    @property
    def exchange(self):
        """Gets the exchange of this Orders.  # noqa: E501


        :return: The exchange of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this Orders.


        :param exchange: The exchange of this Orders.  # noqa: E501
        :type exchange: str
        """
        allowed_values = ["NSE", "BSE", "NSE-FX", "MCX-CM", "NCDEX-CM", "BSE-FX", "MSEI-SX", "MCX-CM", "NCDEX-CM"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and exchange not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `exchange` ({0}), must be one of {1}"  # noqa: E501
                .format(exchange, allowed_values)
            )

        self._exchange = exchange

    @property
    def orderQuantity(self):
        """Gets the orderQuantity of this Orders.  # noqa: E501


        :return: The orderQuantity of this Orders.  # noqa: E501
        :rtype: int
        """
        return self._orderQuantity

    @orderQuantity.setter
    def orderQuantity(self, orderQuantity):
        """Sets the orderQuantity of this Orders.


        :param orderQuantity: The orderQuantity of this Orders.  # noqa: E501
        :type orderQuantity: int
        """

        self._orderQuantity = orderQuantity

    @property
    def pendingQuantity(self):
        """Gets the pendingQuantity of this Orders.  # noqa: E501


        :return: The pendingQuantity of this Orders.  # noqa: E501
        :rtype: int
        """
        return self._pendingQuantity

    @pendingQuantity.setter
    def pendingQuantity(self, pendingQuantity):
        """Sets the pendingQuantity of this Orders.


        :param pendingQuantity: The pendingQuantity of this Orders.  # noqa: E501
        :type pendingQuantity: int
        """

        self._pendingQuantity = pendingQuantity

    @property
    def cancelledQuantity(self):
        """Gets the cancelledQuantity of this Orders.  # noqa: E501


        :return: The cancelledQuantity of this Orders.  # noqa: E501
        :rtype: int
        """
        return self._cancelledQuantity

    @cancelledQuantity.setter
    def cancelledQuantity(self, cancelledQuantity):
        """Sets the cancelledQuantity of this Orders.


        :param cancelledQuantity: The cancelledQuantity of this Orders.  # noqa: E501
        :type cancelledQuantity: int
        """

        self._cancelledQuantity = cancelledQuantity

    @property
    def filledQuantity(self):
        """Gets the filledQuantity of this Orders.  # noqa: E501


        :return: The filledQuantity of this Orders.  # noqa: E501
        :rtype: int
        """
        return self._filledQuantity

    @filledQuantity.setter
    def filledQuantity(self, filledQuantity):
        """Sets the filledQuantity of this Orders.


        :param filledQuantity: The filledQuantity of this Orders.  # noqa: E501
        :type filledQuantity: int
        """

        self._filledQuantity = filledQuantity

    @property
    def disclosedQuantity(self):
        """Gets the disclosedQuantity of this Orders.  # noqa: E501


        :return: The disclosedQuantity of this Orders.  # noqa: E501
        :rtype: int
        """
        return self._disclosedQuantity

    @disclosedQuantity.setter
    def disclosedQuantity(self, disclosedQuantity):
        """Sets the disclosedQuantity of this Orders.


        :param disclosedQuantity: The disclosedQuantity of this Orders.  # noqa: E501
        :type disclosedQuantity: int
        """

        self._disclosedQuantity = disclosedQuantity

    @property
    def triggerPrice(self):
        """Gets the triggerPrice of this Orders.  # noqa: E501


        :return: The triggerPrice of this Orders.  # noqa: E501
        :rtype: int
        """
        return self._triggerPrice

    @triggerPrice.setter
    def triggerPrice(self, triggerPrice):
        """Sets the triggerPrice of this Orders.


        :param triggerPrice: The triggerPrice of this Orders.  # noqa: E501
        :type triggerPrice: int
        """

        self._triggerPrice = triggerPrice

    @property
    def price(self):
        """Gets the price of this Orders.  # noqa: E501


        :return: The price of this Orders.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Orders.


        :param price: The price of this Orders.  # noqa: E501
        :type price: float
        """

        self._price = price

    @property
    def product(self):
        """Gets the product of this Orders.  # noqa: E501


        :return: The product of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this Orders.


        :param product: The product of this Orders.  # noqa: E501
        :type product: str
        """
        allowed_values = ["NORMAL", "SUPERMULTIPLE", "SUPERMULTIPLEOPTION", "MTF", "TSLONEW", "BRACKETNEW", "TSLO", "BRACKET", "GTC", "COD", "CONVERT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and product not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `product` ({0}), must be one of {1}"  # noqa: E501
                .format(product, allowed_values)
            )

        self._product = product

    @property
    def transactionType(self):
        """Gets the transactionType of this Orders.  # noqa: E501


        :return: The transactionType of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._transactionType

    @transactionType.setter
    def transactionType(self, transactionType):
        """Sets the transactionType of this Orders.


        :param transactionType: The transactionType of this Orders.  # noqa: E501
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
    def orderTimestamp(self):
        """Gets the orderTimestamp of this Orders.  # noqa: E501


        :return: The orderTimestamp of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._orderTimestamp

    @orderTimestamp.setter
    def orderTimestamp(self, orderTimestamp):
        """Sets the orderTimestamp of this Orders.


        :param orderTimestamp: The orderTimestamp of this Orders.  # noqa: E501
        :type orderTimestamp: str
        """

        self._orderTimestamp = orderTimestamp

    @property
    def validity(self):
        """Gets the validity of this Orders.  # noqa: E501


        :return: The validity of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this Orders.


        :param validity: The validity of this Orders.  # noqa: E501
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
    def statusMessage(self):
        """Gets the statusMessage of this Orders.  # noqa: E501


        :return: The statusMessage of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._statusMessage

    @statusMessage.setter
    def statusMessage(self, statusMessage):
        """Sets the statusMessage of this Orders.


        :param statusMessage: The statusMessage of this Orders.  # noqa: E501
        :type statusMessage: str
        """

        self._statusMessage = statusMessage

    @property
    def tag(self):
        """Gets the tag of this Orders.  # noqa: E501


        :return: The tag of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Orders.


        :param tag: The tag of this Orders.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

    @property
    def status(self):
        """Gets the status of this Orders.  # noqa: E501

        Order Status  # noqa: E501

        :return: The status of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Orders.

        Order Status  # noqa: E501

        :param status: The status of this Orders.  # noqa: E501
        :type status: str
        """
        allowed_values = ["placed", "approved", "delivered"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def statusInfo(self):
        """Gets the statusInfo of this Orders.  # noqa: E501


        :return: The statusInfo of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._statusInfo

    @statusInfo.setter
    def statusInfo(self, statusInfo):
        """Sets the statusInfo of this Orders.


        :param statusInfo: The statusInfo of this Orders.  # noqa: E501
        :type statusInfo: str
        """

        self._statusInfo = statusInfo

    @property
    def isFNO(self):
        """Gets the isFNO of this Orders.  # noqa: E501


        :return: The isFNO of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._isFNO

    @isFNO.setter
    def isFNO(self, isFNO):
        """Sets the isFNO of this Orders.


        :param isFNO: The isFNO of this Orders.  # noqa: E501
        :type isFNO: str
        """

        self._isFNO = isFNO

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
        if not isinstance(other, Orders):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Orders):
            return True

        return self.to_dict() != other.to_dict()
