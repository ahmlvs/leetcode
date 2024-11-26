import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([2,7,11,15], 9), [1, 2])

    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([2,3,4], 6), [1, 3])

    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([-1,0], -1), [1, 2])
    