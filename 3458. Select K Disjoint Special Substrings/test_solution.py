import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "abcdbaefab"
        k = 2
        expected = True
        solution = Solution()
        self.assertEqual(solution.maxSubstringLength(s, k), expected)
    
    def test_case_2(self):
        s = "cdefdc"
        k = 3
        expected = False
        solution = Solution()
        self.assertEqual(solution.maxSubstringLength(s, k), expected)
    
    def test_case_3(self):
        s = "abeabe"
        k = 0
        expected = True
        solution = Solution()
        self.assertEqual(solution.maxSubstringLength(s, k), expected)
