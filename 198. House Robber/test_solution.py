import unittest
from solution import Solution

class TestResult(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(s.rob([1,2,3,1]), 4)
    
    def test_2(self):
        s = Solution()
        self.assertEqual(s.rob([2,7,9,3,1]), 12)
    
    def test_3(self):
        s = Solution()
        self.assertEqual(s.rob([2,1,1,2]), 4)
