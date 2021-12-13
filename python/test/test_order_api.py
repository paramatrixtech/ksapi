# coding: utf-8




from __future__ import absolute_import

import unittest

import ks_api_client
from ks_api_client.api.order_api import OrderApi  # noqa: E501
from ks_api_client.rest import ApiException

class TestOrderApi(unittest.TestCase):
    """OrderApi unit test stubs"""

    def setUp(self):
        self.api = ks_api_client.api.order_api.OrderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_modify_order(self):
        """Test case for modify_order

        Modify an existing order  # noqa: E501
        """
        pass

    def test_place_new_order(self):
        """Test case for place_new_order

        Place a New order  # noqa: E501
        """
        pass

if __name__ == '__main__':
    unittest.main()
