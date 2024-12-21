import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        board = [[-1, -1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1, -1],
                 [-1, 35, -1, -1, 13, -1],
                 [-1, -1, -1, -1, -1, -1],
                 [-1, 15, -1, -1, -1, -1]]
        expected = 4
        self.assertEqual(Solution().snakesAndLadders(board), expected)
    
    def test_case_2(self):
        board = [[-1, -1],
                 [-1, 3]]
        expected = 1
        self.assertEqual(Solution().snakesAndLadders(board), expected)
    
    def test_case_3(self):
        board = [[-1,-1,30,14,15,-1],
                 [23,9,-1,-1,-1,9],
                 [12,5,7,24,-1,30],
                 [10,-1,-1,-1,25,17],
                 [32,-1,28,-1,-1,32],
                 [-1,-1,23,-1,13,19]]
        expected = 2
        self.assertEqual(Solution().snakesAndLadders(board), expected)
    
    def test_case_4(self):
        board = [[-1,-1,-1],
                 [-1,-1,-1],
                 [-1,-1,-1]]
        expected = 2
        self.assertEqual(Solution().snakesAndLadders(board), expected)
    
    def test_case_5(self):
        board = [[1,1,-1],
                 [1,1,1],
                 [-1,1,1]]
        expected = -1
        self.assertEqual(Solution().snakesAndLadders(board), expected)
