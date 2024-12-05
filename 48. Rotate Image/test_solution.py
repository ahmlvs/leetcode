import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        sol.rotate(matrix)
        self.assertEqual(matrix, [[7,4,1],[8,5,2],[9,6,3]])
    
    def test_case_2(self):
        sol = Solution()
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        sol.rotate(matrix)
        self.assertEqual(matrix, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
