import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "daabcbaabcbc"
        part = "abc"
        expected_result = "dab"
        solution = Solution()
        self.assertEqual(solution.removeOccurrences(s, part), expected_result)
    
    def test_case_2(self):
        s = "axxxxyyyyb"
        part = "xy"
        expected_result = "ab"
        solution = Solution()
        self.assertEqual(solution.removeOccurrences(s, part), expected_result)
