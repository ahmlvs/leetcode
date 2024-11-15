import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(2), 2)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(3), 3)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(1), 1)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(10), 89)
    