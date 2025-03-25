import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        n = 5
        rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
        expected = True
        solution = Solution()
        self.assertEqual(solution.checkValidCuts(n, rectangles), expected)
    
    def test_case_2(self):
        n = 4
        rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
        expected = True
        solution = Solution()
        self.assertEqual(solution.checkValidCuts(n, rectangles), expected)

    def test_case_3(self):
        n = 4
        rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
        expected = False
        solution = Solution()
        self.assertEqual(solution.checkValidCuts(n, rectangles), expected)
