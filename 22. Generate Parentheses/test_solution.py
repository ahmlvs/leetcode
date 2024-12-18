import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        n = 3
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertCountEqual(Solution().generateParenthesis(n), expected)
    
    def test_case_2(self):
        n = 1
        expected = ["()"]
        self.assertCountEqual(Solution().generateParenthesis(n), expected)
    
    def test_case_3(self):
        n = 2
        expected = ["(())", "()()"]
        self.assertCountEqual(Solution().generateParenthesis(n), expected)
