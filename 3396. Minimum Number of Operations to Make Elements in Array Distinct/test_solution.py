import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.minimumOperations([1,2,3,4,2,3,3,5,7]), 2)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.minimumOperations([4,5,6,4,4]), 2)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.minimumOperations([6,7,8,9]), 0)
