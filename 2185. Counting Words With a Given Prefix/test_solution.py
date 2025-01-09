import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.prefixCount(["pay","attention","practice","attend"], "at"), 2)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.prefixCount(["leetcode","win","loops","success"], "code"), 0)
