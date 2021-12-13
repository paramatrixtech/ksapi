# coding: utf-8




from __future__ import absolute_import

import unittest

import ks_api_client
from ks_api_client.api.super_multiple_order_api import SuperMultipleOrderApi  # noqa: E501
from ks_api_client.rest import ApiException


class TestSuperMultipleOrderApi(unittest.TestCase):
    """SuperMultipleOrderApi unit test stubs"""

    def setUp(self):
        self.api = ks_api_client.api.super_multiple_order_api.SuperMultipleOrderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_sm_order(self):
        """Test case for cancel_sm_order

        Cancel an Super Multiple order  # noqa: E501
        """
        pass

    def test_modify_sm_order(self):
        """Test case for modify_sm_order

        Modify an existing super multiple order  # noqa: E501
        """
        pass

    def test_place_new_sm_order(self):
        """Test case for place_new_sm_order

        Place a New Super Multiple order  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
