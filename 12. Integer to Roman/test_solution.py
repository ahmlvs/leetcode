import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        num = 3749
        expected = "MMMDCCXLIX"
        solution = Solution()
        self.assertEqual(solution.intToRoman(num), expected)
    
    def test_case_2(self):
        num = 58
        expected = "LVIII"
        solution = Solution()
        self.assertEqual(solution.intToRoman(num), expected)
    
    def test_case_3(self):
        num = 1994
        expected = "MCMXCIV"
        solution = Solution()
        self.assertEqual(solution.intToRoman(num), expected)
    
    def test_case_4(self):
        num = 108
        expected = "CVIII"
        solution = Solution()
        self.assertEqual(solution.intToRoman(num), expected)
        