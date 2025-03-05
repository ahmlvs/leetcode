import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.coloredCells(1), 1)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.coloredCells(2), 5)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.coloredCells(1000), 1998001)
