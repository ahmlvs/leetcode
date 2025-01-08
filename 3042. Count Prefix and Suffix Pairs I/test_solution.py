import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        words = ["a","aba","ababa","aa"]
        self.assertEqual(sol.countPrefixSuffixPairs(words), 4)

    def test_case_2(self):
        sol = Solution()
        words = ["pa","papa","ma","mama"]
        self.assertEqual(sol.countPrefixSuffixPairs(words), 2)

    def test_case_3(self):
        sol = Solution()
        words = ["abab","ab"]
        self.assertEqual(sol.countPrefixSuffixPairs(words), 0)
