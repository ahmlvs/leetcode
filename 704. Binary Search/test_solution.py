import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.search([-1,0,3,5,9,12], 9), 4)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.search([-1,0,3,5,9,12], 2), -1)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.search([5], 5), 0)
