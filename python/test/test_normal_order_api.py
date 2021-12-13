# coding: utf-8




from __future__ import absolute_import

import unittest

import ks_api_client
from ks_api_client.api.normal_order_api import NormalOrderApi  # noqa: E501
from ks_api_client.rest import ApiException

class TestNormalOrderApi(unittest.TestCase):
    """NormalOrderApi unit test stubs"""

    def setUp(self):
        self.api = ks_api_client.api.normal_order_api.NormalOrderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_normal_order(self):
        """Test case for cancel_normal_order

        Cancel a Normal order  # noqa: E501
        """
        pass

    def test_modify_normal_order(self):
        """Test case for modify_normal_order

        Modify an existing normal order  # noqa: E501
        """
        pass

    def test_place_new_normal_order(self):
        """Test case for place_new_normal_order

        Place a New normal order  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
