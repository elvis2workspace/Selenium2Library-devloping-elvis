import unittest

from Selenium2Library import utils


class UtilsPackageTests(unittest.TestCase):
    def test_escape_xpath_value_with_apos(self):
        self.assertEqual(
            utils.escape_xpath_value("test_selenium2library '1'"),
            "\"test_selenium2library '1'\"")

    def test_escape_xpath_value_with_quote(self):
        self.assertEqual(
            utils.escape_xpath_value("test_selenium2library \"1\""),
            "'test_selenium2library \"1\"'")

    def test_escape_xpath_value_with_quote_and_apos(self):
        self.assertEqual(
            utils.escape_xpath_value("test_selenium2library \"1\" and '2'"),
            "concat('test_selenium2library \"1\" and ', \"'\", '2', \"'\", '')")
