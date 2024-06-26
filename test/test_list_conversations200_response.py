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

from aihub.models.list_conversations200_response import ListConversations200Response

class TestListConversations200Response(unittest.TestCase):
    """ListConversations200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListConversations200Response:
        """Test ListConversations200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConversations200Response`
        """
        model = ListConversations200Response()
        if include_optional:
            return ListConversations200Response(
                conversations = [
                    aihub.models.conversation_summary.conversationSummary(
                        id = '', 
                        name = '', 
                        description = '', )
                    ]
            )
        else:
            return ListConversations200Response(
        )
        """

    def testListConversations200Response(self):
        """Test ListConversations200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
