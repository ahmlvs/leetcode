import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.evalRPN(["2","1","+","3","*"]), 9)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.evalRPN(["4","13","5","/","+"]), 6)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.evalRPN(["4"]), 4)
    