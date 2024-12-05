import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.singleNumber([2,2,3,2]), 3)
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.singleNumber([0,1,0,1,0,1,99]), 99)
