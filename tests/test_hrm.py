# Tests for the HRM module

import unittest
from src.hrm.model import HRM

class TestHRM(unittest.TestCase):

    def setUp(self):
        self.hrm = HRM()

    def test_query_hello(self):
        response = self.hrm.query("hello")
        self.assertEqual(response, "Hello! How can I help you today?")

    def test_query_time(self):
        response = self.hrm.query("what time is it?")
        self.assertEqual(response, "I am sorry, I cannot tell the time yet.")

    def test_query_unknown(self):
        response = self.hrm.query("what is your name?")
        self.assertEqual(response, "I am not sure how to respond to that.")

    def test_query_case_insensitivity(self):
        response = self.hrm.query("HELLO")
        self.assertEqual(response, "Hello! How can I help you today?")

if __name__ == '__main__':
    unittest.main()
