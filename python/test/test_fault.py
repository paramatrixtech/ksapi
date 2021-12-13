# coding: utf-8




from __future__ import absolute_import

import unittest
import datetime

import ks_api_client
from ks_api_client.models.fault import Fault  # noqa: E501
from ks_api_client.rest import ApiException

class TestFault(unittest.TestCase):
    """Fault unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Fault
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        model = ks_api_client.models.fault.Fault()  # noqa: E501
        if include_optional :
            return Fault(
                code = 56, 
                message = '0', 
                description = '0'
            )
        else :
            return Fault(
        )

    def testFault(self):
        """Test Fault"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
