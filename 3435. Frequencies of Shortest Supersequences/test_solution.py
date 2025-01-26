import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        words = ["ab","ba"]
        expected = [[1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        solution = Solution()
        self.assertListEqual(solution.supersequences(words), expected)
    
    def test_case_2(self):
        words = ["aa","ac"]
        expected = [[2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        solution = Solution()
        self.assertListEqual(solution.supersequences(words), expected)
    
    def test_case_3(self):
        words = ["aa","bb","cc"]
        expected = [[2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        solution = Solution()
        self.assertListEqual(solution.supersequences(words), expected)
