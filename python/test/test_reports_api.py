# coding: utf-8




from __future__ import absolute_import

import unittest
import time
import ks_api_client
from ks_api_client.ks_api import KSTradeApi as TradingApi
from ks_api_client.rest import ApiException
from ks_api_client.settings import host, access_token, userid, \
    consumer_key, app_id, password, access_code, ip

class TestReportsApi(unittest.TestCase):
    """ReportsApi unit test stubs"""
    ks_trade_api = TradingApi(access_token, userid, consumer_key, ip, app_id, host)

    def setUp(self):
        self.ks_trade_api.login(password = password)
        self.ks_trade_api.session_2fa(access_code = access_code)

    def tearDown(self):
        pass

    def test_get_fno_order_detail_by_order_id(self):
        """Test case for get_fno_order_detail_by_order_id

        Get order report by orderId  # noqa: E501
        """
        place_new_order = self.ks_trade_api.place_order(order_type = "N", tag = "string", transaction_type = "BUY", \
                    instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                    disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        order_id = place_new_order['Success']['NSE']['orderId']
        if order_id:
            fno_order_details = self.ks_trade_api.order_report(order_id = order_id,is_fno = "Y")
            print("FNO Order Details: ",fno_order_details)

    def test_get_order_report_by_order_id(self):
        """Test case for get_order_report_by_order_id

        Get order report by orderId  # noqa: E501
        """
        place_new_order = self.ks_trade_api.place_order(order_type = "N", tag = "string", transaction_type = "BUY", \
                    instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                    disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        order_id = place_new_order['Success']['NSE']['orderId']
        if order_id:
            order_report = self.ks_trade_api.order_report(order_id = order_id)
            print("Order Report: ",order_report)

    def test_get_order_reports(self):
        """Test case for get_order_reports

        Get order report  # noqa: E501
        """
        order_reports = self.ks_trade_api.order_report()
        print("Order Reports: ",order_reports)

    def test_get_trade_report(self):
        """Test case for get_trade_report

        Get trade report  # noqa: E501
        """
        trade_reports = self.ks_trade_api.trade_report()
        print("Trade Reports: ",trade_reports)

    def test_get_trade_report_by_order_id(self):
        """Test case for get_trade_report_by_order_id

        Get trade report by orderId  # noqa: E501
        """
        place_new_order = self.ks_trade_api.place_order(order_type = "N", tag = "string", transaction_type = "BUY", \
                            instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                            disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        order_id = place_new_order['Success']['NSE']['orderId']
        if order_id:
            trade_report = self.ks_trade_api.trade_report(order_id=order_id)
            print("Trade Report",trade_report)

    def test_get_fno_trade_detail_by_order_id(self):
        """Test case for get_fno_order_detail_by_order_id

        Get order report by orderId  # noqa: E501
        """
        place_new_order = self.ks_trade_api.place_order(order_type = "N", tag = "string", transaction_type = "BUY", \
                            instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                            disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        order_id = place_new_order['Success']['NSE']['orderId']
        if order_id:
            fno_trade_report = self.ks_trade_api.order_report(order_id = order_id,is_fno = "Y")
            print("fno_trade_details: ",fno_trade_report)


if __name__ == '__main__':
    unittest.main()
