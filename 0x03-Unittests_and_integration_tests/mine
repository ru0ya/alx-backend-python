#!/usr/bin/env python3
"""
Method to test for correct value
"""


import utils
import unittests
from parameterized import parameterized
from utils import get_json
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """
    class with methods that test for correct value
    """
    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """
        Test organisation:
        Arguments: input- organisations to test for
                   mock: Mock object
        """
        test = GithubOrgClient(input)
        test.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')
