import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
        entrance = [1,2]
        expected = 1
        self.assertEqual(Solution().nearestExit(maze, entrance), expected)

    def test_case_2(self):
        maze = [["+","+","+"],[".",".","."],["+","+","+"]]
        entrance = [1,0]
        expected = 2
        self.assertEqual(Solution().nearestExit(maze, entrance), expected)

    def test_case_3(self):
        maze = [[".","+"]]
        entrance = [0,0]
        expected = -1
        self.assertEqual(Solution().nearestExit(maze, entrance), expected)
