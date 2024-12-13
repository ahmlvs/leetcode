import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.threeSum([0,1,1]), [])
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.threeSum([0,0,0]), [[0,0,0]])
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.threeSum([0,0,0,0,0,0]), [[0,0,0]])
