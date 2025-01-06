import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        expected = ["eat","oath"]
        self.assertCountEqual(sol.findWords(board, words), expected)
    
    def test_case_2(self):
        sol = Solution()
        board = [["a","b"],["c","d"]]
        words = ["abcb"]
        expected = []
        self.assertCountEqual(sol.findWords(board, words), expected)
