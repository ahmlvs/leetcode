import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        grid = [[3,2,1],[1,7,6],[2,7,7]]
        self.assertEqual(self.solution.equalPairs(grid), 1)
    
    def test_case_2(self):
        grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
        self.assertEqual(self.solution.equalPairs(grid), 3)
    
    def test_case_3(self):
        grid = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(self.solution.equalPairs(grid), 0)
