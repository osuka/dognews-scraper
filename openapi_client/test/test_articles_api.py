"""
    Dognews Server API

    Dognews Server client API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.articles_api import ArticlesApi  # noqa: E501


class TestArticlesApi(unittest.TestCase):
    """ArticlesApi unit test stubs"""

    def setUp(self):
        self.api = ArticlesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_articles_list(self):
        """Test case for articles_list

        """
        pass

    def test_articles_retrieve(self):
        """Test case for articles_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
