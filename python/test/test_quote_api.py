# coding: utf-8




from __future__ import absolute_import

import unittest

import ks_api_client
from ks_api_client.api.quote_api import QuoteApi  # noqa: E501
from ks_api_client.rest import ApiException


class TestQuoteApi(unittest.TestCase):
    """QuoteApi unit test stubs"""

    def setUp(self):
        self.api = ks_api_client.api.quote_api.QuoteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_instruments_details(self):
        """Test case for get_instruments_details

        Get full details  # noqa: E501
        """
        pass

    def test_get_ltp_quote(self):
        """Test case for get_ltp_quote

        Get LTP quote  # noqa: E501
        """
        pass

    def test_get_market_details_quote(self):
        """Test case for get_market_details_quote

        Get market details quote  # noqa: E501
        """
        pass

    def test_get_ohlc_quote(self):
        """Test case for get_ohlc_quote

        Get OHLC quote  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
