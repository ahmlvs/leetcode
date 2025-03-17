import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.divideArray([3,2,3,2,2,2]), True)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.divideArray([1,2,3,4]), False)
