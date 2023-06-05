import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test access_nested_map function to ensure it returns
        the value associated with the provided key path in the nested map
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
        Test access_nested_map function to ensure it
        raises a KeyError for the given inputs
        """
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(err.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """
    Unit tests for the get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json function to ensure it returns the expected result
        """
        mock_get.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the memoize decorator
    """

    def test_memoize(self):
        """
        Test the memoize decorator to ensure
        it caches the result of the decorated method
        """
        class TestClass:
            @memoize
            def a_method(self):
                return 42

            @property
            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once()
