import unittest

import HtmlTestRunner

from Week5.tests.simplebookstests.test_api_status import TestApiStatus
from Week5.tests.simplebookstests.test_get_all_books import TestGetAllBooks
from Week5.tests.simplebookstests.test_submit_order import TestSubmitOrder
from Week5.tests.simplebookstests.test_update_order import TestUpdateOrder


class TestSuite(unittest.TestCase):

    def test_suite(self):
        suita_teste = unittest.TestSuite()

        suita_teste.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestApiStatus),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetAllBooks),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSubmitOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestUpdateOrder),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Api test report",
            report_name="Books API Test Results"
        )

        runner.run(suita_teste)
