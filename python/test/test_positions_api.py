# coding: utf-8




from __future__ import absolute_import

import unittest
import ks_api_client
from ks_api_client.api.positions_api import PositionsApi  # noqa: E501
from ks_api_client.rest import ApiException

class TestPositionsApi(unittest.TestCase):
    """PositionsApi unit test stubs"""

    def setUp(self):
        self.api = ks_api_client.api.positions_api.PositionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_positions(self):
        """Test case for positions

        Get's raw position from Trading Engine.  # noqa: E501
        """
        pass

    def test_positions_open(self):
        """Test case for positions_open

        Get's Open position.  # noqa: E501
        """
        pass

    def test_positions_stocks(self):
        """Test case for positions_stocks

        Get's Sell from Existing stocks.  # noqa: E501
        """
        pass

    def test_positions_today(self):
        """Test case for positions_today

        Get's Todays position.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
