import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        self.assertCountEqual(sol.combinationSum(candidates, target), expected)

    def test_case_2(self):
        sol = Solution()
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertCountEqual(sol.combinationSum(candidates, target), expected)

    def test_case_3(self):
        sol = Solution()
        candidates = [2]
        target = 1
        expected = []
        self.assertCountEqual(sol.combinationSum(candidates, target), expected)
