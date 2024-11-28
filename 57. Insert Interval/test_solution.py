import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        self.assertEqual(sol.insert(intervals, newInterval), [[1, 5], [6, 9]])
    
    def test_case_2(self):
        sol = Solution()
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        self.assertEqual(sol.insert(intervals, newInterval), [[1, 2], [3, 10], [12, 16]])
    
    def test_case_3(self):
        sol = Solution()
        intervals = []
        newInterval = [5, 7]
        self.assertEqual(sol.insert(intervals, newInterval), [[5, 7]])
    