import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.numWaterBottles(9, 3), 13)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.numWaterBottles(15, 4), 19)
