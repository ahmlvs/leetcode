import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        nums1 = [1,3,3,2]
        nums2 = [2,1,3,4]
        k = 3
        output = 12
        solution = Solution()
        self.assertEqual(solution.maxScore(nums1, nums2, k), output)
    
    def test_2(self):
        nums1 = [4,2,3,1,1]
        nums2 = [7,5,10,9,6]
        k = 1
        output = 30
        solution = Solution()
        self.assertEqual(solution.maxScore(nums1, nums2, k), output)
    
    def test_3(self):
        nums1 = [1,2,3,4,5]
        nums2 = [6,7,8,9,10]
        k = 5
        output = 90
        solution = Solution()
        self.assertEqual(solution.maxScore(nums1, nums2, k), output)
