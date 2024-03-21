# coding: utf-8

"""
    AIHub API

    The AIHub REST API. Please see https://aihub.instabase.com/docs/ for more details.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from aihub.models.conversation_summary import ConversationSummary

class TestConversationSummary(unittest.TestCase):
    """ConversationSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConversationSummary:
        """Test ConversationSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConversationSummary`
        """
        model = ConversationSummary()
        if include_optional:
            return ConversationSummary(
                id = '',
                name = '',
                description = ''
            )
        else:
            return ConversationSummary(
                id = '',
                name = '',
        )
        """

    def testConversationSummary(self):
        """Test ConversationSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()