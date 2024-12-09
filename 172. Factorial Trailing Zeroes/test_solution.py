import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 3
        expected = 0
        self.assertEqual(sol.trailingZeroes(n), expected)
    
    def test_case_2(self):
        sol = Solution()
        n = 5
        expected = 1
        self.assertEqual(sol.trailingZeroes(n), expected)
    
    def test_case_3(self):
        sol = Solution()
        n = 0
        expected = 0
        self.assertEqual(sol.trailingZeroes(n), expected)
    
    def test_case_4(self):
        sol = Solution()
        n = 120
        expected = 28
        self.assertEqual(sol.trailingZeroes(n), expected)
