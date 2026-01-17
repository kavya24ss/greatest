# test_greatest.py
# Tests for the simple greatest number program using max()

import unittest

def find_greatest(a, b, c):
    return max(a, b, c)

class TestGreatest(unittest.TestCase):

    def test_first_is_greatest(self):
        self.assertEqual(find_greatest(12, 5, 3), 12)

    def test_second_is_greatest(self):
        self.assertEqual(find_greatest(4, 15, 9), 15)

    def test_third_is_greatest(self):
        self.assertEqual(find_greatest(7, 8, 20), 20)

    def test_all_equal(self):
        self.assertEqual(find_greatest(10, 10, 10), 10)

    def test_two_equal_greatest(self):
        self.assertEqual(find_greatest(25, 25, 10), 25)

if __name__ == "__main__":
    unittest.main()
