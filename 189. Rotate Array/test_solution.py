import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        sol.rotate(nums, k)
        self.assertListEqual(nums, [5, 6, 7, 1, 2, 3, 4])
    
    def test_case_2(self):
        sol = Solution()
        nums = [-1, -100, 3, 99]
        k = 2
        sol.rotate(nums, k)
        self.assertListEqual(nums, [3, 99, -1, -100])
    
    def test_case_3(self):
        sol = Solution()
        nums = [1, 2]
        k = 3
        sol.rotate(nums, k)
        self.assertListEqual(nums, [2, 1])
    