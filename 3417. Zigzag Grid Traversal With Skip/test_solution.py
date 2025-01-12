import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[1,2],[3,4]]
        self.assertEqual(sol.zigzagTraversal(grid), [1,4])
    
    def test_case_2(self):
        sol = Solution()
        grid = [[2,1],[2,1],[2,1]]
        self.assertEqual(sol.zigzagTraversal(grid), [2,1,2])
    
    def test_case_3(self):
        sol = Solution()
        grid = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(sol.zigzagTraversal(grid), [1,3,5,7,9])
