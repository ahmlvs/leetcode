import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1,2]
        k = 1
        self.assertEqual(sol.maxSubarraySum(nums, k), 3)
    
    def test_case_2(self):
        sol = Solution()
        nums = [-1,-2,-3,-4,-5]
        k = 4
        self.assertEqual(sol.maxSubarraySum(nums, k), -10)
    
    def test_case_3(self):
        sol = Solution()
        nums = [-5,1,2,-3,4]
        k = 2
        self.assertEqual(sol.maxSubarraySum(nums, k), 4)
