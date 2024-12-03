import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([5,7,7,8,8,10], 8), [3, 4])
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([5,7,7,8,8,10], 6), [-1, -1])
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([], 0), [-1, -1])
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([1], 1), [0, 0])
