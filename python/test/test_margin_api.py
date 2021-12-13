# coding: utf-8




from __future__ import absolute_import

import unittest

import ks_api_client
from ks_api_client.api.margin_api import MarginApi  # noqa: E501
from ks_api_client.ks_api import KSTradeApi as TradingApi
from ks_api_client.rest import ApiException
from ks_api_client.settings import host, access_token, userid, \
    consumer_key, app_id, password, access_code, ip

class TestMarginApi(unittest.TestCase):
    """MarginApi unit test stubs"""
    ks_trade_api = TradingApi(access_token, userid, consumer_key, ip, app_id, host)
    ks_trade_api.login(password = password)
    ks_trade_api.session_2fa(access_code = access_code)

    def setUp(self):
        self.api = ks_api_client.api.margin_api.MarginApi()  # noqa: E501
        self.ks_trade_api.login(password)
        self.ks_trade_api.session_2fa(access_code)

    def tearDown(self):
        pass

    def test_get_margins(self):
        """Test case for get_margins

        Complete Margin  # noqa: E501
        """
        margin = self.ks_trade_api.margin()
        print("Margin : ",margin)

    def test_margin_required(self):
        """Test case for margin_required

        Get Margin Required for an order by amount or quantity.  # noqa: E501
        """
        order_info = [
            {"instrument_token": 727, "quantity": 1, "price": 1300, "amount": 0, "trigger_price": 1190},
            {"instrument_token": 1374, "quantity": 1, "price": 1200, "amount": 0, "trigger_price": 1150}
            ]
        margin_required = self.ks_trade_api.margin_required(transaction_type = "BUY",order_info = order_info)
        print("Margin required: ",margin_required)

if __name__ == '__main__':
    unittest.main()
