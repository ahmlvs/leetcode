import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        word = "aeioqq"
        k = 1
        self.assertEqual(sol.countOfSubstrings(word, k), 0)
    
    def test_case_2(self):
        sol = Solution()
        word = "aeiou"
        k = 0
        self.assertEqual(sol.countOfSubstrings(word, k), 1)
    
    def test_case_3(self):
        sol = Solution()
        word = "ieaouqqieaouqq"
        k = 1
        self.assertEqual(sol.countOfSubstrings(word, k), 3)
