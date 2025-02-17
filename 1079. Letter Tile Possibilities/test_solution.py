import unittest
from solution import Solution


class TestResult(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.numTilePossibilities("AAB"), 8)
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.numTilePossibilities("AAABBC"), 188)
    
    def test_case_3(self):
        solution = Solution()
        self.assertEqual(solution.numTilePossibilities("V"), 1)
