import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_uniquePaths(self):
        solution = Solution()
        self.assertEqual(solution.uniquePaths(3, 7), 28)
    
    def test_uniquePaths_2(self):
        solution = Solution()
        self.assertEqual(solution.uniquePaths(3, 2), 3)
