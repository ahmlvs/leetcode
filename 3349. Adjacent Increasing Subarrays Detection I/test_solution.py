import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3), True)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7], 5), False)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.hasIncreasingSubarrays([-15,19], 1), True)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.hasIncreasingSubarrays([19,-15], 1), True)
    
    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.hasIncreasingSubarrays([5,8,-2,-1], 2), True)
    