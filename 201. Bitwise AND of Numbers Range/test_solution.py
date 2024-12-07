import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.rangeBitwiseAnd(5, 7), 4)
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.rangeBitwiseAnd(0, 0), 0)
    
    def test_case_3(self):
        solution = Solution()
        self.assertEqual(solution.rangeBitwiseAnd(1, 2147483647), 0)
