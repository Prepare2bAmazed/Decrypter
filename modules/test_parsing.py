import unittest
import modules.parsing as p
import modules.classes as c
from deepdiff import DeepDiff
import modules.encryption as e

class TestParsing(unittest.TestCase):
    def test_list_to_json_to_list(self):
        starting_list = [c.UrlUserPass("amazon.com", "Steve123", "amazonPass11"),
                         c.UrlUserPass("bestbuy.com", "SteveW", "bestbuyPass22"),
                         c.UrlUserPass("dell.com", "StevenWalt", "dellPass44")]

        expected_json_string = '[{"url": "amazon.com", "username": "Steve123", "password": "amazonPass11"}, {"url": "bestbuy.com", "username": "SteveW", "password": "bestbuyPass22"}, {"url": "dell.com", "username": "StevenWalt", "password": "dellPass44"}]'
        actual_json_string = p.uup_list_to_json(starting_list)
        actual_json_to_list = p.json_to_uup_list(actual_json_string)

        diff = DeepDiff(starting_list, actual_json_to_list)
        self.assertEqual(expected_json_string, actual_json_string)
        self.assertEqual(diff, {})

    def test_encrypted_to_list(self):
        starting_json = '[{"url": "amazon.com", "username": "Steve123", "password": "amazonPass11"}, {"url": "bestbuy.com", "username": "SteveW", "password": "bestbuyPass22"}, {"url": "dell.com", "username": "StevenWalt", "password": "dellPass44"}]'
        password = "ThePassword"
        encrypted_json = e.encode(starting_json, password)
        expected_list = [c.UrlUserPass("amazon.com", "Steve123", "amazonPass11"),
                         c.UrlUserPass("bestbuy.com", "SteveW", "bestbuyPass22"),
                         c.UrlUserPass("dell.com", "StevenWalt", "dellPass44")]
        actual_list = p.encrypted_contents_to_list(encrypted_json, password)

        diff = DeepDiff(actual_list, expected_list)
        self.assertEqual(diff, {})
