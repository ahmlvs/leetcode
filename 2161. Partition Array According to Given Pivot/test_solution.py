import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.pivotArray([9,12,5,10,14,3,10], 10), [9,5,3,10,10,12,14])

    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.pivotArray([-3,4,3,2], 2), [-3,2,4,3])
