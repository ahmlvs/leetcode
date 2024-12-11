import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        expected = 4
        self.assertEqual(sol.maximalSquare(matrix), expected)
    
    def test_case_2(self):
        sol = Solution()
        matrix = [["0","1"],["1","0"]]
        expected = 1
        self.assertEqual(sol.maximalSquare(matrix), expected)
    
    def test_case_3(self):
        sol = Solution()
        matrix = [["0"]]
        expected = 0
        self.assertEqual(sol.maximalSquare(matrix), expected)
