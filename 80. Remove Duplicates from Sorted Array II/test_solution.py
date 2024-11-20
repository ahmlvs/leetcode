import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1,1,1,2,2,3]
        expected = 5
        expected_nums = [1,1,2,2,3]
        k = sol.removeDuplicates(nums)
        self.assertEqual(k, expected)
        self.assertEqual(nums[:k], expected_nums)
    
    def test_case_2(self):
        sol = Solution()
        nums = [0,0,1,1,1,1,2,3,3]
        expected = 7
        expected_nums = [0,0,1,1,2,3,3]
        k = sol.removeDuplicates(nums)
        self.assertEqual(k, expected)
        self.assertEqual(nums[:k], expected_nums)
    
    def test_case_3(self):
        sol = Solution()
        nums = [1,2,3]
        expected = 3
        expected_nums = [1,2,3]
        k = sol.removeDuplicates(nums)
        self.assertEqual(k, expected)
        self.assertEqual(nums[:k], expected_nums)
    