import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.closestPrimes(10, 19), [11, 13])
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.closestPrimes(4, 6), [-1, -1])
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.closestPrimes(10, 100000), [11, 13])
