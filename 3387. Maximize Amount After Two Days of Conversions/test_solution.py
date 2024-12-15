import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        initialCurrency = "EUR"
        pairs1 = [["EUR","USD"],["USD","JPY"]]
        rates1 = [2.0,3.0]
        pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]]
        rates2 = [4.0,5.0,6.0]
        expected = 720.00000
        solution = Solution()
        self.assertEqual(solution.maxAmount(initialCurrency, pairs1, rates1, pairs2, rates2), expected)
    
    def test_case_2(self):
        initialCurrency = "NGN"
        pairs1 = [["NGN","EUR"]]
        rates1 = [9.0]
        pairs2 = [["NGN","EUR"]]
        rates2 = [6.0]
        expected = 1.50000
        solution = Solution()
        self.assertEqual(solution.maxAmount(initialCurrency, pairs1, rates1, pairs2, rates2), expected)
    
    def test_case_3(self):
        initialCurrency = "USD"
        pairs1 = [["USD","EUR"]]
        rates1 = [1.0]
        pairs2 = [["EUR","JPY"]]
        rates2 = [10.0]
        expected = 1.00000
        solution = Solution()
        self.assertEqual(solution.maxAmount(initialCurrency, pairs1, rates1, pairs2, rates2), expected)
