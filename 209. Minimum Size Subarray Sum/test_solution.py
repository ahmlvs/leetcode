import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        self.assertEqual(sol.minSubArrayLen(7, [2,3,1,2,4,3]), 2)
    
    def test_case2(self):
        sol = Solution()
        self.assertEqual(sol.minSubArrayLen(4, [1,4,4]), 1)
    
    def test_case3(self):
        sol = Solution()
        self.assertEqual(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]), 0)
