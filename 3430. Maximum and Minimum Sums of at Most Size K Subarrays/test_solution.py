import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1,2,3]
        k = 2
        expected = 20
        self.assertEqual(sol.minMaxSubarraySum(nums, k), expected)
    
    def test_case_2(self):
        sol = Solution()
        nums = [1,-3,1]
        k = 2
        expected = -6
        self.assertEqual(sol.minMaxSubarraySum(nums, k), expected)
