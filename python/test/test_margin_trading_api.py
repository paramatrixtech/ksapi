# coding: utf-8




from __future__ import absolute_import

import unittest

import ks_api_client
from ks_api_client.ks_api import KSTradeApi as TradingApi
from ks_api_client.api.margin_trading_api import MarginTradingApi  # noqa: E501
from ks_api_client.rest import ApiException
from ks_api_client.settings import host, access_token, userid, \
    consumer_key, app_id, password, access_code, ip

class TestMarginTradingApi(unittest.TestCase):
    """MarginTradingApi unit test stubs"""

    def setUp(self):
        self.api = ks_api_client.api.margin_trading_api.MarginTradingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_mtf_order(self):
        """Test case for cancel_mtf_order

        Cancel an order  # noqa: E501
        """
        pass

    def test_modify_mtf_order(self):
        """Test case for modify_mtf_order

        Modify an existing MTF order  # noqa: E501
        """
        pass

    def test_place_new_mtf_order(self):
        """Test case for place_new_mtf_order

        Place a New MTF order  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
