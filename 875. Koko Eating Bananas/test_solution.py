import unittest
from solution import Solution

class TestResult(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(s.minEatingSpeed([3,6,7,11], 8), 4)
    
    def test_2(self):
        s = Solution()
        self.assertEqual(s.minEatingSpeed([30,11,23,4,20], 5), 30)
    
    def test_3(self):
        s = Solution()
        self.assertEqual(s.minEatingSpeed([30,11,23,4,20], 6), 23)
    
    def test_4(self):
        s = Solution()
        self.assertEqual(s.minEatingSpeed([312884470], 312884469), 2)
    
    def test_5(self):
        s = Solution()
        self.assertEqual(s.minEatingSpeed([805306368,805306368,805306368], 1000000000), 3)
