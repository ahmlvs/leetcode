import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonSubsequence("abcde", "ace"), 3)
    
    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonSubsequence("abc", "abc"), 3)
    
    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonSubsequence("abc", "def"), 0)
    
    def test_4(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonSubsequence("a", "a"), 1)
    
    def test_5(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonSubsequence("a", "b"), 0)
    
    def test_6(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonSubsequence("ab", "b"), 1)
    
    def test_7(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonSubsequence("bsbininm", "jmjkbkjkv"), 1)
    