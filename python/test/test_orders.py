# coding: utf-8




from __future__ import absolute_import

import unittest
import datetime

import ks_api_client
from ks_api_client.models.orders import Orders  # noqa: E501
from ks_api_client.rest import ApiException

class TestOrders(unittest.TestCase):
    """Orders unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Orders
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        model = ks_api_client.models.orders.Orders()  # noqa: E501
        if include_optional :
            return Orders(
                orderId = 1.337, 
                variety = 'REGULAR', 
                instrumentName = '0', 
                instrumentToken = '0', 
                exchange = 'NSE', 
                orderQuantity = 56, 
                pendingQuantity = 56, 
                cancelledQuantity = 56, 
                filledQuantity = 56, 
                disclosedQuantity = 56, 
                triggerPrice = 56, 
                price = 1.337, 
                product = 'NORMAL', 
                transactionType = 'BUY', 
                orderTimestamp = '0', 
                validity = 'GFD', 
                statusMessage = '0', 
                tag = '0', 
                status = 'placed', 
                statusInfo = '0', 
                isFNO = '0'
            )
        else :
            return Orders(
        )

    def testOrders(self):
        """Test Orders"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
