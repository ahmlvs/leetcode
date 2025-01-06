import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.maxLength([1,2,1,2,1,1,1]), 5)
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.maxLength([2,3,4,5,6]), 3)
    
    def test_case_3(self):
        solution = Solution()
        self.assertEqual(solution.maxLength([1,2,3,1,4,5,1]), 5)
    
    def test_case_4(self):
        solution = Solution()
        self.assertEqual(solution.maxLength([1,1,1,1,1,1,1]), 7)
