import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        A = [1,3,2,4]
        B = [3,1,2,4]
        expected = [0,2,3,4]
        solution = Solution()
        self.assertListEqual(solution.findThePrefixCommonArray(A, B), expected)
    
    def test_case_2(self):
        A = [2,3,1]
        B = [3,1,2]
        expected = [0,1,3]
        solution = Solution()
        self.assertListEqual(solution.findThePrefixCommonArray(A, B), expected)
    
    def test_case_3(self):
        A = [1]
        B = [1]
        expected = [1]
        solution = Solution()
        self.assertListEqual(solution.findThePrefixCommonArray(A, B), expected)
    
    def test_case_4(self):
        A = [1,2,3,4,5]
        B = [1,2,3,4,5]
        expected = [1,2,3,4,5]
        solution = Solution()
        self.assertListEqual(solution.findThePrefixCommonArray(A, B), expected)
