import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        result = sol.spiralOrder(matrix)
        self.assertEqual(result, [1,2,3,6,9,8,7,4,5])
    
    def test_case_2(self):
        sol = Solution()
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        result = sol.spiralOrder(matrix)
        self.assertEqual(result, [1,2,3,4,8,12,11,10,9,5,6,7])
    
    def test_case_3(self):
        sol = Solution()
        matrix = [[1]]
        result = sol.spiralOrder(matrix)
        self.assertEqual(result, [1])
    
    def test_case_4(self):
        sol = Solution()
        matrix = [[1,2],[3,4]]
        result = sol.spiralOrder(matrix)
        self.assertEqual(result, [1,2,4,3])
    