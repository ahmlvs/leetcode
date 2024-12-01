import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        nums = [2,3,5,10]
        expected = 10
        self.assertEqual(solution.getLargestOutlier(nums), expected)

    def test_case_2(self):
        solution = Solution()
        nums = [-2,-1,-3,-6,4]
        expected = 4
        self.assertEqual(solution.getLargestOutlier(nums), expected)

    def test_case_3(self):
        solution = Solution()
        nums = [1,1,1,1,1,5,5]
        expected = 5
        self.assertEqual(solution.getLargestOutlier(nums), expected)
