import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.minDistance("horse", "ros"), 3)
    
    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.minDistance("intention", "execution"), 5)
    
    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.minDistance("aaa", "aaa"), 0)
    