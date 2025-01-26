import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.countPartitions([10,10,3,7,6]), 4)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.countPartitions([1,2,2]), 0)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.countPartitions([2,4,6,8]), 3)
