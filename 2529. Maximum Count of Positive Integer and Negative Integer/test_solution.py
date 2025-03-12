import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.maximumCount([-2,-1,-1,1,2,3]), 3)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.maximumCount([-3,-2,-1,0,0,1,2]), 3)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.maximumCount([5,20,66,1314]), 4)
