import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit([1,3,2,8,4,9], 2), 8)
    
    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit([1,3,7,5,10,3], 3), 6)
    
    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit([1,1], 2), 0)
