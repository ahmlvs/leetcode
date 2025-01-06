import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "aczzx"
        self.assertEqual(sol.calculateScore(s), 5)

    def test_case_2(self):
        sol = Solution()
        s = "abcdef"
        self.assertEqual(sol.calculateScore(s), 0)
