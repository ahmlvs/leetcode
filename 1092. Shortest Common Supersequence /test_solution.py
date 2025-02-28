import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        str1 = "abac"
        str2 = "cab"
        self.assertEqual(sol.shortestCommonSupersequence(str1, str2), "cabac")
    
    def test_case_2(self):
        sol = Solution()
        str1 = "aaaaaaaa"
        str2 = "aaaaaaaa"
        self.assertEqual(sol.shortestCommonSupersequence(str1, str2), "aaaaaaaa")
