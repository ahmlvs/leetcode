import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.maximumSum([18,43,36,13,7]), 54)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.maximumSum([10,12,19,14]), -1)
