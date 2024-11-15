import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        ans = round(sol.myPow(2.00000, 10), 5)
        self.assertEqual(ans, 1024.00000)
    
    def test_case_2(self):
        sol = Solution()
        ans = round(sol.myPow(2.10000, 3), 5)
        self.assertEqual(ans, 9.26100)
    
    def test_case_3(self):
        sol = Solution()
        ans = round(sol.myPow(2.00000, -2), 5)
        self.assertEqual(ans, 0.25000)
    
    def test_case_4(self):
        sol = Solution()
        ans = round(sol.myPow(0.00001, 2147483647), 5)
        self.assertEqual(ans, 0.00000)
    
    def test_case_5(self):
        sol = Solution()
        ans = round(sol.myPow(-2.00000, -2), 5)
        self.assertEqual(ans, 0.25000)
    
    def test_case_6(self):
        sol = Solution()
        ans = round(sol.myPow(0.00000, 1), 5)
        self.assertEqual(ans, 0.00000)
