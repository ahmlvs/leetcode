import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        points = [[1,1],[2,2],[3,3]]
        expected = 3
        self.assertEqual(sol.maxPoints(points), expected)

    def test_case_2(self):
        sol = Solution()
        points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        expected = 4
        self.assertEqual(sol.maxPoints(points), expected)

    def test_case_3(self):
        sol = Solution()
        points = [[0,0]]
        expected = 1
        self.assertEqual(sol.maxPoints(points), expected)
