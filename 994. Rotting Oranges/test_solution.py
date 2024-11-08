import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        self.assertEqual(sol.orangesRotting(grid), 4)
    
    def test_case_2(self):
        sol = Solution()
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        self.assertEqual(sol.orangesRotting(grid), -1)
    
    def test_case_3(self):
        sol = Solution()
        grid = [[0, 2]]
        self.assertEqual(sol.orangesRotting(grid), 0)
