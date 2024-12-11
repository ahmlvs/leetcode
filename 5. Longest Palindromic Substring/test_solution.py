import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "babad"
        expected = "aba"
        solution = Solution()
        self.assertEqual(solution.longestPalindrome(s), expected)
    
    def test_case_2(self):
        s = "cbbd"
        expected = "bb"
        solution = Solution()
        self.assertEqual(solution.longestPalindrome(s), expected)
    
    def test_case_3(self):
        s = "a"
        expected = "a"
        solution = Solution()
        self.assertEqual(solution.longestPalindrome(s), expected)
    
    def test_case_4(self):
        s = "abcd"
        expected = "a"
        solution = Solution()
        self.assertEqual(solution.longestPalindrome(s), expected)
    
    def test_case_5(self):
        s = "aaaa"
        expected = "aaaa"
        solution = Solution()
        self.assertEqual(solution.longestPalindrome(s), expected)
