import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.maximumCandies([5,8,6], 3), 5)

    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.maximumCandies([2,5], 11), 0)
