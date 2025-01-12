import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
        expected = 8
        self.assertEqual(sol.maximumAmount(coins), expected)
    
    def test_case_2(self):
        sol = Solution()
        coins = [[10, 10, 10], [10, 10, 10]]
        expected = 40
        self.assertEqual(sol.maximumAmount(coins), expected)
