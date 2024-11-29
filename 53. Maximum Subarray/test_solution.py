import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([1]), 1)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([5,4,-1,7,8]), 23)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([-10]), -10)
    
    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([-10,2]), 2)
    