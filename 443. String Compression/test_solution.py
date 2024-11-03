import unittest
from solution import Solution

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        chars = ["a","a","b","b","c","c","c"]
        self.assertEqual(self.solution.compress(chars), 6)
        self.assertEqual(chars[:6], ["a","2","b","2","c","3"])
    
    def test_case_2(self):
        chars = ["a"]
        self.assertEqual(self.solution.compress(chars), 1)
        self.assertEqual(chars[:1], ["a"])
    
    def test_case_3(self):
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        self.assertEqual(self.solution.compress(chars), 4)
        self.assertEqual(chars[:4], ["a","b","1","2"])
