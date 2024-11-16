import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertListEqual(solution.plusOne([1, 2, 3]), [1, 2, 4])
    
    def test_case_2(self):
        solution = Solution()
        self.assertListEqual(solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
    
    def test_case_3(self):
        solution = Solution()
        self.assertListEqual(solution.plusOne([9]), [1, 0])
    
    def test_case_4(self):
        solution = Solution()
        self.assertListEqual(solution.plusOne([9, 9]), [1, 0, 0])
