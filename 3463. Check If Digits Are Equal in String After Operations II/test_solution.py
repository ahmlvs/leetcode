import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "3902"
        expected = True
        solution = Solution()
        self.assertEqual(solution.hasSameDigits(s), expected)
    
    def test_case_2(self):
        s = "34789"
        expected = False
        solution = Solution()
        self.assertEqual(solution.hasSameDigits(s), expected)
