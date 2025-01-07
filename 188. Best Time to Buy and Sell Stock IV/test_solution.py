import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit(2, [2,4,1]), 2)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit(2, [3,2,6,5,0,3]), 7)
