import unittest

import HtmlTestRunner

from Week2.unitest import Test


class TestSuite(unittest.TestCase):

    @unittest.skip
    def test_suite(self):
        tests_suite = unittest.TestSuite()
        tests_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Test))
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title='TestReport', report_name='FullTest')
        runner.run(tests_suite)

    def test_suite_2(self):
        tests_suite = unittest.TestSuite()
        tests_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Test))
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title='TestReport', report_name='FullTest')
        runner.run(tests_suite)
