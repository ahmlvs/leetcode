import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        expected_result = 5
        solution = Solution()
        self.assertEqual(solution.ladderLength(beginWord, endWord, wordList), expected_result)
    
    def test_case_2(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        expected_result = 0
        solution = Solution()
        self.assertEqual(solution.ladderLength(beginWord, endWord, wordList), expected_result)
    
    def test_case_3(self):
        beginWord = "hit"
        endWord = "hot"
        wordList = ["hot"]
        expected_result = 2
        solution = Solution()
        self.assertEqual(solution.ladderLength(beginWord, endWord, wordList), expected_result)
