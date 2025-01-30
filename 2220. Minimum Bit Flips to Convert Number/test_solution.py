import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.minBitFlips(10, 7), 3)

    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.minBitFlips(3, 4), 3)
