import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.isPerfectSquare(16), True)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.isPerfectSquare(14), False)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.isPerfectSquare(2147483647), False)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.isPerfectSquare(808201), True)