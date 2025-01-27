import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.distributeCandies([1,1,2,2,3,3]), 3)
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.distributeCandies([1,1,2,3]), 2)
    
    def test_case_3(self):
        solution = Solution()
        self.assertEqual(solution.distributeCandies([6,6,6,6]), 1)
