import unittest
from scripts.process_data import process_data
import os

class TestProcessData(unittest.TestCase):
    def test_process_data(self):
        process_data()
        self.assertTrue(os.path.exists('data/processed_data.csv'))

if __name__ == "__main__":
    unittest.main()
