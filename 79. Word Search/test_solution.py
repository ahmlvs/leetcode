import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        self.assertEqual(sol.exist(board, word), True)
    
    def test_case_2(self):
        sol = Solution()
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "SEE"
        self.assertEqual(sol.exist(board, word), True)
    
    def test_case_3(self):
        sol = Solution()
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCB"
        self.assertEqual(sol.exist(board, word), False)
