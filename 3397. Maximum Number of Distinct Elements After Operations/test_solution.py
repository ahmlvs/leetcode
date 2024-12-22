import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.maxDistinctElements([1,2,2,3,3,4], 2), 6)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.maxDistinctElements([4,4,4,4], 1), 3)
