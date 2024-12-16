import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "abcabcbb"
        expected = 3
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring(s), expected)
    
    def test_case_2(self):
        s = "bbbbb"
        expected = 1
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring(s), expected)
    
    def test_case_3(self):
        s = "pwwkew"
        expected = 3
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring(s), expected)
