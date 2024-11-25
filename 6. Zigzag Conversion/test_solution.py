import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "PAYPALISHIRING"
        numRows = 3
        expected_result = "PAHNAPLSIIGYIR"
        solution = Solution()
        result = solution.convert(s, numRows)
        self.assertEqual(result, expected_result)

    def test_case_2(self):
        s = "PAYPALISHIRING"
        numRows = 4
        expected_result = "PINALSIGYAHRPI"
        solution = Solution()
        result = solution.convert(s, numRows)
        self.assertEqual(result, expected_result)

    def test_case_3(self):
        s = "A"
        numRows = 1
        expected_result = "A"
        solution = Solution()
        result = solution.convert(s, numRows)
        self.assertEqual(result, expected_result)
    
    def test_case_4(self):
        s = "AB"
        numRows = 1
        expected_result = "AB"
        solution = Solution()
        result = solution.convert(s, numRows)
        self.assertEqual(result, expected_result)
    