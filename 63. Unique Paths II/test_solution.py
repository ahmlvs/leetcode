import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
        expected = 2
        self.assertEqual(sol.uniquePathsWithObstacles(obstacleGrid), expected)
    
    def test_case_2(self):
        sol = Solution()
        obstacleGrid = [[0,1],[0,0]]
        expected = 1
        self.assertEqual(sol.uniquePathsWithObstacles(obstacleGrid), expected)

    def test_case_3(self):
        sol = Solution()
        obstacleGrid = [[0,0,0],[0,0,0],[0,0,0]]
        expected = 6
        self.assertEqual(sol.uniquePathsWithObstacles(obstacleGrid), expected)
    
    def test_case_4(self):
        sol = Solution()
        obstacleGrid = [[0]]
        expected = 1
        self.assertEqual(sol.uniquePathsWithObstacles(obstacleGrid), expected)
    
    def test_case_5(self):
        sol = Solution()
        obstacleGrid = [[1,0,0]]
        expected = 0
        self.assertEqual(sol.uniquePathsWithObstacles(obstacleGrid), expected)
    
    def test_case_6(self):
        sol = Solution()
        obstacleGrid = [[0,1,0]]
        expected = 0
        self.assertEqual(sol.uniquePathsWithObstacles(obstacleGrid), expected)
    