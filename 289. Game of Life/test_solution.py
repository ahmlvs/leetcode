import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        expected = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        Solution().gameOfLife(board)
        self.assertEqual(board, expected)
    
    def test_case_2(self):
        board = [[1,1],[1,0]]
        expected = [[1,1],[1,1]]
        Solution().gameOfLife(board)
        self.assertEqual(board, expected)
    
    def test_case_3(self):
        board = [[1,1],[1,1]]
        expected = [[1,1],[1,1]]
        Solution().gameOfLife(board)
        self.assertEqual(board, expected)
    
    def test_case_4(self):
        board = [[1]]
        expected = [[0]]
        Solution().gameOfLife(board)
        self.assertEqual(board, expected)
    
    def test_case_5(self):
        board = [[0]]
        expected = [[0]]
        Solution().gameOfLife(board)
        self.assertEqual(board, expected)
