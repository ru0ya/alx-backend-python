#!/usr/bin/env python3
"""
Parametize a unit test
Unit test for utils.access_nested_map
"""


import unittest
from parameterized import parameterized


access_nested_map = __import__('utils').access_nested_map


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
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

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

        self.assertEqual(str(err.exception), f"'{path[-1]}'")
