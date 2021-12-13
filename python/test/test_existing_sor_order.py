# coding: utf-8




from __future__ import absolute_import

import unittest
import datetime

import ks_api_client
from ks_api_client.models.existing_sor_order import ExistingSOROrder  # noqa: E501
from ks_api_client.rest import ApiException

class TestExistingSOROrder(unittest.TestCase):
    """ExistingSOROrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExistingSOROrder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
#        model = ks_api_client.models.existing_sor_order.ExistingSOROrder()  # noqa: E501
        if include_optional :
            return ExistingSOROrder(
                orderId = '0', 
                quantity = 56, 
                price = 1.337, 
                disclosedQuantity = 56, 
                triggerPrice = 1.337, 
                validity = 'GFD'
            )
        else :
            return ExistingSOROrder(
                orderId = '0',
        )

    def testExistingSOROrder(self):
        """Test ExistingSOROrder"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
