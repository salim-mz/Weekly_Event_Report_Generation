import unittest
from scripts.fetch_data import fetch_data
import os

class TestFetchData(unittest.TestCase):
    def test_fetch_data(self):
        fetch_data()
        self.assertTrue(os.path.exists('data/raw_data.json'))

if __name__ == "__main__":
    unittest.main()
