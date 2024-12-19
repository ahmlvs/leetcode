import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        Solution().solve(board)
        self.assertEqual(
            board,
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"]
            ]
        )
    
    def test_case_2(self):
        board = [
            ["X"]
        ]
        Solution().solve(board)
        self.assertEqual(
            board,
            [
                ["X"]
            ]
        )
    
    def test_case_3(self):
        board = [
            ["O","O"],
            ["O","O"]
        ]
        Solution().solve(board)
        self.assertEqual(
            board,
            [
                ["O","O"],
                ["O","O"]
            ]
        )
    
    def test_case_4(self):
        board = [["X","O","X"],["O","X","O"],["X","O","X"]]
        Solution().solve(board)
        self.assertEqual(
            board,
            [["X","O","X"],["O","X","O"],["X","O","X"]]
        )
