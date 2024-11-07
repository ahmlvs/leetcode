import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        k = 3
        n = 7
        output = [[1,2,4]]
        self.assertEqual(Solution().combinationSum3(k, n), output)
    
    def test_2(self):
        k = 3
        n = 9
        output = [[1,2,6],[1,3,5],[2,3,4]]
        self.assertEqual(Solution().combinationSum3(k, n), output)
    
    def test_3(self):
        k = 4
        n = 1
        output = []
        self.assertEqual(Solution().combinationSum3(k, n), output)
