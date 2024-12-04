import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.search([4,5,6,7,0,1,2], 0), 4)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.search([4,5,6,7,0,1,2], 3), -1)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.search([1], 0), -1)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.search([1], 1), 0)
    
    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.search([5,1,3], 3), 2)
