import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.fib(2), 1)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.fib(3), 2)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.fib(4), 3)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.fib(0), 0)
    
    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.fib(1), 1)
    
    def test_case_6(self):
        sol = Solution()
        self.assertEqual(sol.fib(30), 832040)
    
    def test_case_7(self):
        sol = Solution()
        self.assertEqual(sol.fib(100), 354224848179261915075)
