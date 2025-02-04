import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.maxAscendingSum([10,20,30,5,10,50]), 65)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.maxAscendingSum([10,20,30,40,50]), 150)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.maxAscendingSum([12,17,15,13,10,11,12]), 33)
