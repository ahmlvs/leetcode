import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        digits = "23"
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertCountEqual(Solution().letterCombinations(digits), expected)
    
    def test_2(self):
        digits = ""
        expected = []
        self.assertCountEqual(Solution().letterCombinations(digits), expected)
    
    def test_3(self):
        digits = "2"
        expected = ["a","b","c"]
        self.assertCountEqual(Solution().letterCombinations(digits), expected)
