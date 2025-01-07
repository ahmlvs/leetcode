import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.findMedianSortedArrays([1, 3], [2]), 2.0)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.findMedianSortedArrays([1, 2], [3, 4]), 2.5)
