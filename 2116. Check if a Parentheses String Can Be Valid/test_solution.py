import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "))()))"
        locked = "010100"

        self.assertEqual(sol.canBeValid(s, locked), True)
    
    def test_case_2(self):
        sol = Solution()
        s = "()()"
        locked = "0000"

        self.assertEqual(sol.canBeValid(s, locked), True)
    
    def test_case_3(self):
        sol = Solution()
        s = ")"
        locked = "0"

        self.assertEqual(sol.canBeValid(s, locked), False)
    
    def test_case_4(self):
        sol = Solution()
        s = "()))"
        locked = "0010"

        self.assertEqual(sol.canBeValid(s, locked), True)
    
    def test_case_5(self):
        sol = Solution()
        s = "())()))()(()(((())(()()))))((((()())(())"
        locked = "1011101100010001001011000000110010100101"

        self.assertEqual(sol.canBeValid(s, locked), True)
