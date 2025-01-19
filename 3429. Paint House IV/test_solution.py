import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        n = 4
        cost = [[3,5,7],[6,2,9],[4,8,1],[7,3,5]]
        expected = 9
        self.assertEqual(Solution().minCost(n, cost), expected)
    
    def test_case_2(self):
        n = 6
        cost = [[2,4,6],[5,3,8],[7,1,9],[4,6,2],[3,5,7],[8,2,4]]
        expected = 18
        self.assertEqual(Solution().minCost(n, cost), expected)
