import unittest
from scripts.generate_report import generate_report
import os

class TestGenerateReport(unittest.TestCase):
    def test_generate_report(self):
        generate_report()
        self.assertTrue(os.path.exists('reports/weekly_event_report.xlsx'))

if __name__ == "__main__":
    unittest.main()
