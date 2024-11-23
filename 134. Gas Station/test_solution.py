import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]), 3)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.canCompleteCircuit([2,3,4], [3,4,3]), -1)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.canCompleteCircuit([2,3,5], [3,4,3]), 2)
    