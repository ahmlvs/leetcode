import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.longestCommonPrefix(["flower","flow","flight"]), "fl")
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.longestCommonPrefix(["dog","racecar","car"]), "")
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.longestCommonPrefix(["dog","dog","dog"]), "dog")
