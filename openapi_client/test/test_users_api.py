"""
    Dognews Server API

    Dognews Server client API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_create(self):
        """Test case for users_create

        """
        pass

    def test_users_destroy(self):
        """Test case for users_destroy

        """
        pass

    def test_users_list(self):
        """Test case for users_list

        """
        pass

    def test_users_partial_update(self):
        """Test case for users_partial_update

        """
        pass

    def test_users_retrieve(self):
        """Test case for users_retrieve

        """
        pass

    def test_users_update(self):
        """Test case for users_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
