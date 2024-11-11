import unittest
from solution import Solution



class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        haystack = "sadbutsad"
        needle = "sad"
        self.assertEqual(sol.strStr(haystack, needle), 0)
    
    def test_case_2(self):
        sol = Solution()
        haystack = "leetcode"
        needle = "leeto"
        self.assertEqual(sol.strStr(haystack, needle), -1)
    
    def test_case_3(self):
        sol = Solution()
        haystack = "leetcode"
        needle = "leet"
        self.assertEqual(sol.strStr(haystack, needle), 0)
    
    def test_case_4(self):
        sol = Solution()
        haystack = "leetcode"
        needle = "code"
        self.assertEqual(sol.strStr(haystack, needle), 4)
