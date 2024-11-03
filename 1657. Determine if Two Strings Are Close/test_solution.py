import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        word1 = "abc"
        word2 = "bca"
        self.assertTrue(self.solution.closeStrings(word1, word2))

    def test_case_2(self):
        word1 = "a"
        word2 = "aa"
        self.assertFalse(self.solution.closeStrings(word1, word2))
    
    def test_case_3(self):
        word1 = "cabbba"
        word2 = "abbccc"
        self.assertTrue(self.solution.closeStrings(word1, word2))
