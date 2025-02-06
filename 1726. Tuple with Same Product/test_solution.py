import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.tupleSameProduct([2,3,4,6]), 8)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.tupleSameProduct([1,2,4,5,10]), 16)
