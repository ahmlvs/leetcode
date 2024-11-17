import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 0, 1]
        queries = [[0, 2]]
        self.assertEqual(sol.isZeroArray(nums, queries), True)
    
    def test_case_2(self):
        sol = Solution()
        nums = [4, 3, 2, 1]
        queries = [[1, 3], [0, 2]]
        self.assertEqual(sol.isZeroArray(nums, queries), False)
    
    def test_case_3(self):
        sol = Solution()
        nums = [1, 1, 1]
        queries = [[0, 2]]
        self.assertEqual(sol.isZeroArray(nums, queries), True)
    