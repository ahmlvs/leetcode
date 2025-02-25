import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.numOfSubarrays([1,3,5]), 4)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.numOfSubarrays([2,4,6]), 0)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.numOfSubarrays([1,2,3,4,5,6,7]), 16)
