import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        points = [[1,1],[1,3],[3,1],[3,3]]
        expected = 4
        s = Solution()
        self.assertEqual(s.maxRectangleArea(points), expected)
    
    def test_case_2(self):
        points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
        expected = -1
        s = Solution()
        self.assertEqual(s.maxRectangleArea(points), expected)
    
    def test_case_3(self):
        points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]
        expected = 2
        s = Solution()
        self.assertEqual(s.maxRectangleArea(points), expected)
