import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        nums = [3, -2, 1, 4]
        l = 2
        r = 3
        expected = 1
        s = Solution()
        self.assertEqual(s.minimumSumSubarray(nums, l, r), expected)
    
    def test_case_2(self):
        nums = [-2, 2, -3, 1]
        l = 2
        r = 3
        expected = -1
        s = Solution()
        self.assertEqual(s.minimumSumSubarray(nums, l, r), expected)
    
    def test_case_3(self):
        nums = [1, 2, 3, 4]
        l = 2
        r = 4
        expected = 3
        s = Solution()
        self.assertEqual(s.minimumSumSubarray(nums, l, r), expected)
    