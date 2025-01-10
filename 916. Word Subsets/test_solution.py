import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["e", "o"]
        self.assertListEqual(sol.wordSubsets(words1, words2), ["facebook", "google", "leetcode"])
    
    def test_case_2(self):
        sol = Solution()
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["l", "e"]
        self.assertListEqual(sol.wordSubsets(words1, words2), ["apple", "google", "leetcode"])
    
    def test_case_3(self):
        sol = Solution()
        words1 = ["aaaba","aabcb","cbcca","abcca","ccaca"]
        words2 = ["ac","b","b"]
        self.assertListEqual(sol.wordSubsets(words1, words2), ["aabcb","cbcca","abcca"])
