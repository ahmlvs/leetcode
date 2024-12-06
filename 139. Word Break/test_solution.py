import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "leetcode"
        wordDict = ["leet","code"]
        self.assertEqual(sol.wordBreak(s, wordDict), True)
    
    def test_case_2(self):
        sol = Solution()
        s = "applepenapple"
        wordDict = ["apple","pen"]
        self.assertEqual(sol.wordBreak(s, wordDict), True)
    
    def test_case_3(self):
        sol = Solution()
        s = "catsandog"
        wordDict = ["cats","dog","sand","and","cat"]
        self.assertEqual(sol.wordBreak(s, wordDict), False)
