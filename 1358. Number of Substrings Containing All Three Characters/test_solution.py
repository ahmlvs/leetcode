import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "abcabc"
        expected = 10
        self.assertEqual(sol.numberOfSubstrings(s), expected)
    
    def test_case_2(self):
        sol = Solution()
        s = "aaacb"
        expected = 3
        self.assertEqual(sol.numberOfSubstrings(s), expected)
    
    def test_case_3(self):
        sol = Solution()
        s = "abc"
        expected = 1
        self.assertEqual(sol.numberOfSubstrings(s), expected)
