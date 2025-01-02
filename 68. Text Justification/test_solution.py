import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        expected = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
        self.assertListEqual(Solution().fullJustify(words, maxWidth), expected)
    
    def test_case_2(self):
        words = ["What","must","be","acknowledgment","shall","be"]
        maxWidth = 16
        expected = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        self.assertListEqual(Solution().fullJustify(words, maxWidth), expected)
    
    def test_case_3(self):
        words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
        maxWidth = 20
        expected = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]
        self.assertListEqual(Solution().fullJustify(words, maxWidth), expected)
