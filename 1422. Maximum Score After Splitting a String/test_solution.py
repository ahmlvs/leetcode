import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "011101"
        expected = 5
        sol = Solution()
        self.assertEqual(sol.maxScore(s), expected)
    
    def test_case_2(self):
        s = "00111"
        expected = 5
        sol = Solution()
        self.assertEqual(sol.maxScore(s), expected)
    
    def test_case_3(self):
        s = "1111"
        expected = 3
        sol = Solution()
        self.assertEqual(sol.maxScore(s), expected)
    
    def test_case_4(self):
        s = "00"
        expected = 1
        sol = Solution()
        self.assertEqual(sol.maxScore(s), expected)
