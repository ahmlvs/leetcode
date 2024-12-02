import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        Solution().setZeroes(matrix)
        self.assertListEqual(matrix, [[1,0,1],[0,0,0],[1,0,1]])
    
    def test_case_2(self):
        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        Solution().setZeroes(matrix)
        self.assertListEqual(matrix, [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
    