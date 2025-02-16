import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.hasSpecialSubstring("aaabaaa", 3), True)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.hasSpecialSubstring("abc", 2), False)
