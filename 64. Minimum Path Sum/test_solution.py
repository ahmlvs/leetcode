import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        self.assertEqual(sol.minPathSum(grid), 7)
    
    def test_case_2(self):
        sol = Solution()
        grid = [[1,2,3],[4,5,6]]
        self.assertEqual(sol.minPathSum(grid), 12)
    
    def test_case_3(self):
        sol = Solution()
        grid = [[1,2,3]]
        self.assertEqual(sol.minPathSum(grid), 6)
    
    def test_case_4(self):
        sol = Solution()
        grid = [[1],[2],[3]]
        self.assertEqual(sol.minPathSum(grid), 6)
