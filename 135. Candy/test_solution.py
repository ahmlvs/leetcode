import unittest
from solution import Solution

class TestResult(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.candy([1,0,2]), 5)
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.candy([1,2,2]), 4)
    
    def test_case_3(self):
        solution = Solution()
        self.assertEqual(solution.candy([1,2,3,4,5]), 15)
    
    def test_case_4(self):
        solution = Solution()
        self.assertEqual(solution.candy([1, 2, 3, 2, 1]), 9)
