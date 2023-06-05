#!/usr/bin/env python3
"""
Parametize a unit test
Unit test for utils.access_nested_map
"""


import unittest
from unittest import mock
from parameterized import parameterized
from utils import get_json


from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Implements method to test that the method
    returns what it is supposed to
    """
    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Tests acces_nested_map to ensure it returns
        value associated with provided key path in
        nested map
        """
        self.assertEqual(access_nested_map(nested_map, path),
                         expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"), 1)
        ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_result):
        """
        Uses assertRaises to test that a KeyError is
        raised for the inputs
        """
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)

        self.assertEqual(err.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """
    Methods to test if result is expected
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @mock.patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Tests that utils.get_json returns expected result
        """
        mock_get.return_value = test_payload

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Memoization"""
    def test_memoize():
        """memoize method"""

        class TestClass:
            """class"""
            @mock.patch('utils.memoize')
            def a_method(self):
                """method"""
                return 42

            @memoize
            """property"""
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once
