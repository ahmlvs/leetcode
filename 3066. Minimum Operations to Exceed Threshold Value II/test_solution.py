import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.minOperations([2,11,10,1,3], 10), 2)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.minOperations([1,1,2,4,9], 20), 4)
