import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        side = 2
        points = [[0,2],[2,0],[2,2],[0,0]]
        k = 4
        expected = 2
        sol = Solution()
        self.assertEqual(sol.maxDistance(side, points, k), expected)
    
    def test_case_2(self):
        side = 2
        points = [[0,0],[1,2],[2,0],[2,2],[2,1]]
        k = 4
        expected = 1
        sol = Solution()
        self.assertEqual(sol.maxDistance(side, points, k), expected)
    
    def test_case_3(self):
        side = 2
        points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]]
        k = 5
        expected = 1
        sol = Solution()
        self.assertEqual(sol.maxDistance(side, points, k), expected)
    
    def test_case_4(self):
        side = 16
        points = [[0,7],[8,0],[16,16],[1,0],[16,4]]
        k = 4
        expected = 12
        sol = Solution()
        self.assertEqual(sol.maxDistance(side, points, k), expected)
