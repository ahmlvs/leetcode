import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.maxWeight([1,2,3,4,5,6,7,8]), 14)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.maxWeight([2,1,1,1,1,1,1,1]), 3)
