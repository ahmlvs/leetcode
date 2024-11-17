import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.countValidSelections([1,0,2,0,3]), 2)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.countValidSelections([2,3,4,0,4,1,0]), 0)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.countValidSelections([1,0]), 1)
    