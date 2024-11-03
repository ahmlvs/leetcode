import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [1,1,0,1]
        self.assertEqual(self.solution.longestSubarray(nums), 3)
    
    def test_case_2(self):
        nums = [0,1,1,1,0,1,1,0,1]
        self.assertEqual(self.solution.longestSubarray(nums), 5)
    
    def test_case_3(self):
        nums = [1,1,1]
        self.assertEqual(self.solution.longestSubarray(nums), 2)
    
    def test_case_4(self):
        nums = [0,0,0]
        self.assertEqual(self.solution.longestSubarray(nums), 0)
