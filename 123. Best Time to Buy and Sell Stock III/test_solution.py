import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([3,3,5,0,0,3,1,4]), 6)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([1,2,3,4,5]), 4)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([7,6,4,3,1]), 0)
