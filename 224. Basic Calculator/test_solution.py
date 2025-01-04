import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "1 + 1"
        expected = 2
        solution = Solution()
        self.assertEqual(solution.calculate(s), expected)
    
    def test_case_2(self):
        s = " 2-1 + 2 "
        expected = 3
        solution = Solution()
        self.assertEqual(solution.calculate(s), expected)
    
    def test_case_3(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        expected = 23
        solution = Solution()
        self.assertEqual(solution.calculate(s), expected)
    
    def test_case_4(self):
        s = "-(2 + 3)"
        expected = -5
        solution = Solution()
        self.assertEqual(solution.calculate(s), expected)
