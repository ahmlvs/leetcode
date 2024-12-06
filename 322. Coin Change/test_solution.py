import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        coins = [1,2,5]
        amount = 11
        expected = 3
        self.assertEqual(sol.coinChange(coins, amount), expected)
    
    def test_case_2(self):
        sol = Solution()
        coins = [2]
        amount = 3
        expected = -1
        self.assertEqual(sol.coinChange(coins, amount), expected)
    
    def test_case_3(self):
        sol = Solution()
        coins = [1]
        amount = 0
        expected = 0
        self.assertEqual(sol.coinChange(coins, amount), expected)
    
    def test_case_4(self):
        sol = Solution()
        coins = [186,419,83,408]
        amount = 6249
        expected = 20
        self.assertEqual(sol.coinChange(coins, amount), expected)
