import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.isArraySpecial([1]), True)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.isArraySpecial([2,1,4]), True)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.isArraySpecial([4,3,1,6]), False)
