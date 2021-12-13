# coding: utf-8




from __future__ import absolute_import

import unittest
import datetime

import ks_api_client
from ks_api_client.models.new_sm_order import NewSMOrder  # noqa: E501
from ks_api_client.rest import ApiException

class TestNewSMOrder(unittest.TestCase):
    """NewSMOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NewSMOrder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        model = ks_api_client.models.new_sm_order.NewSMOrder()  # noqa: E501
        if include_optional :
            return NewSMOrder(
                instrumentToken = 56, 
                transactionType = 'BUY', 
                quantity = 56, 
                price = 1.337, 
                validity = 'GFD', 
                variety = 'REGULAR', 
                disclosedQuantity = 56, 
                triggerPrice = 1.337, 
                tag = '0'
            )
        else :
            return NewSMOrder(
        )

    def testNewSMOrder(self):
        """Test NewSMOrder"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
