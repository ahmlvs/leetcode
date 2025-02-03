import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.longestMonotonicSubarray([1, 4, 3, 3, 2]), 2)
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.longestMonotonicSubarray([3, 3, 3, 3]), 1)
    
    def test_case_3(self):
        solution = Solution()
        self.assertEqual(solution.longestMonotonicSubarray([3, 2, 1]), 3)
