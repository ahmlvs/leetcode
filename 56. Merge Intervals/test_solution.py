import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        self.assertEqual(sol.merge(intervals), expected)
    
    def test_case2(self):
        sol = Solution()
        intervals = [[1,4],[4,5]]
        expected = [[1,5]]
        self.assertEqual(sol.merge(intervals), expected)

    def test_case3(self):
        sol = Solution()
        intervals = [[1,4],[0,4]]
        expected = [[0,4]]
        self.assertEqual(sol.merge(intervals), expected)
    
    def test_case4(self):
        sol = Solution()
        intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
        expected = [[1,10]]
        self.assertEqual(sol.merge(intervals), expected)
    