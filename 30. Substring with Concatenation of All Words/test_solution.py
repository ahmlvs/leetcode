import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        expected = [0, 9]
        solution = Solution()
        self.assertListEqual(solution.findSubstring(s, words), expected)
    
    def test_case_2(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "word"]
        expected = []
        solution = Solution()
        self.assertListEqual(solution.findSubstring(s, words), expected)
    
    def test_case_3(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "the"]
        expected = [6, 9, 12]
        solution = Solution()
        self.assertListEqual(solution.findSubstring(s, words), expected)
