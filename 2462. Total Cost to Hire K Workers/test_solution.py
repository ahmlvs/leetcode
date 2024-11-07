import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        costs = [17,12,10,2,7,2,11,20,8]
        k = 3
        candidates = 4
        self.assertEqual(Solution().totalCost(costs, k, candidates), 11)
    
    def test_2(self):
        costs = [1,2,4,1]
        k = 3
        candidates = 3
        self.assertEqual(Solution().totalCost(costs, k, candidates), 4)
    
    def test_3(self):
        costs = [1]
        k = 1
        candidates = 1
        self.assertEqual(Solution().totalCost(costs, k, candidates), 1)
