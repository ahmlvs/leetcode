import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.clearDigits("abc"), "abc")
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.clearDigits("cb34"), "")
