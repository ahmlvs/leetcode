import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        word = "dbca"
        numFriends = 2
        expected = "dbc"
        solution = Solution()
        self.assertEqual(expected, solution.answerString(word, numFriends))
    
    def test_case_2(self):
        word = "gggg"
        numFriends = 4
        expected = "g"
        solution = Solution()
        self.assertEqual(expected, solution.answerString(word, numFriends))
    
    def test_case_3(self):
        word = "bif"
        numFriends = 2
        expected = "if"
        solution = Solution()
        self.assertEqual(expected, solution.answerString(word, numFriends))
    
    def test_case_4(self):
        word = "gh"
        numFriends = 1
        expected = "gh"
        solution = Solution()
        self.assertEqual(expected, solution.answerString(word, numFriends))
