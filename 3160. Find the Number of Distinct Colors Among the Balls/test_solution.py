import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        limit = 4
        queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
        expected = [1, 2, 2, 3]
        solution = Solution()
        self.assertListEqual(solution.queryResults(limit, queries), expected)

    def test_case_2(self):
        limit = 4
        queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
        expected = [1, 2, 2, 3, 4]
        solution = Solution()
        self.assertListEqual(solution.queryResults(limit, queries), expected)
