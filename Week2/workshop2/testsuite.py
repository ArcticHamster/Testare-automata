import unittest

from Week2.unitest import Test


class TestSuite(unittest.TestCase):
    def test_suite(self):
        tests_suite = unittest.TestSuite
        tests_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Test))