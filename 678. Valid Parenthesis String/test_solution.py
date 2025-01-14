import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "()"
        self.assertEqual(sol.checkValidString(s), True)
    
    def test_case_2(self):
        sol = Solution()
        s = "(*)"
        self.assertEqual(sol.checkValidString(s), True)
    
    def test_case_3(self):
        sol = Solution()
        s = "(*))"
        self.assertEqual(sol.checkValidString(s), True)
    
    def test_case_4(self):
        sol = Solution()
        s = "(((((*)))**"
        self.assertEqual(sol.checkValidString(s), True)
