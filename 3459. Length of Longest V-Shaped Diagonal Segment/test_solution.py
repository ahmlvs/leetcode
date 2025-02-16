import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
        expected = 5
        s = Solution()
        self.assertEqual(s.lenOfVDiagonal(grid), expected)
    
    def test_case_2(self):
        grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
        expected = 4
        s = Solution()
        self.assertEqual(s.lenOfVDiagonal(grid), expected)
    
    def test_case_3(self):
        grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
        expected = 5
        s = Solution()
        self.assertEqual(s.lenOfVDiagonal(grid), expected)
    
    def test_case_4(self):
        grid = [[1]]
        expected = 1
        s = Solution()
        self.assertEqual(s.lenOfVDiagonal(grid), expected)
