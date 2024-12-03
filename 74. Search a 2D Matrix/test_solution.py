import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 3
        self.assertEqual(sol.searchMatrix(matrix, target), True)
    
    def test_case_2(self):
        sol = Solution()
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 13
        self.assertEqual(sol.searchMatrix(matrix, target), False)
    
    def test_case_3(self):
        sol = Solution()
        matrix = [[1]]
        target = 1
        self.assertEqual(sol.searchMatrix(matrix, target), True)
    
    def test_case_4(self):
        sol = Solution()
        matrix = [[1]]
        target = 2
        self.assertEqual(sol.searchMatrix(matrix, target), False)
    