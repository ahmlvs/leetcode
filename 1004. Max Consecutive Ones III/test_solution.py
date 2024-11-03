import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [1,1,1,0,0,0,1,1,1,1,0]
        k = 2
        expected = 6
        self.assertEqual(self.solution.longestOnes(nums, k), expected)
    
    def test_case_2(self):
        nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        k = 3
        expected = 10
        self.assertEqual(self.solution.longestOnes(nums, k), expected)
    
    def test_case_3(self):
        nums = [0,0,0,1]
        k = 4
        expected = 4
        self.assertEqual(self.solution.longestOnes(nums, k), expected)

    def test_case_4(self):
        nums = [0,0,0,1]
        k = 0
        expected = 1
        self.assertEqual(self.solution.longestOnes(nums, k), expected)
