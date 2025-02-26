import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.maxAbsoluteSum([1,-3,2,3,-4]), 5)
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.maxAbsoluteSum([2,-5,1,-4,3,-2]), 8)
