import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "3902"
        expected_result = True
        solution = Solution()
        result = solution.hasSameDigits(s)
        self.assertEqual(result, expected_result)
    
    def test_case_2(self):
        s = "34789"
        expected_result = False
        solution = Solution()
        result = solution.hasSameDigits(s)
        self.assertEqual(result, expected_result)
