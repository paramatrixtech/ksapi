# coding: utf-8




from __future__ import absolute_import

import unittest

import ks_api_client
from ks_api_client.api.smart_order_routing_api import SmartOrderRoutingApi  # noqa: E501
from ks_api_client.rest import ApiException


class TestSmartOrderRoutingApi(unittest.TestCase):
    """SmartOrderRoutingApi unit test stubs"""

    def setUp(self):
        self.api = ks_api_client.api.smart_order_routing_api.SmartOrderRoutingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_sor_order(self):
        """Test case for cancel_sor_order

        Cancel an SORorder  # noqa: E501
        """
        pass

    def test_modify_sor_order(self):
        """Test case for modify_sor_order

        Modify an existing SOR order  # noqa: E501
        """
        pass

    def test_place_new_sor_order(self):
        """Test case for place_new_sor_order

        Place a New SOR order  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
