import unittest
from bomahut import min_max_numbers

class TestMinMaxNumbers(unittest.TestCase):
    def test_correcteness(self):
        actual = min_max_numbers([[5,16,20],[9,11,18],[15,16,17]])
        expected = [17]
        self.assertEqual(actual, expected)

    def test_empty_matrix(self):
        actual = min_max_numbers([])
        expected = []
        self.assertEqual(actual, expected)