import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertListEqual(sol.nextGreaterElement([4,1,2], [1,3,4,2]), [-1,3,-1])
    
    def test_case_2(self):
        sol = Solution()
        self.assertListEqual(sol.nextGreaterElement([2,4], [1,2,3,4]), [3,-1])
