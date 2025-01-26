import unittest
from solution import Solution

class TestResult(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.maxFrequency([1,2,3,4,5,6], 1), 2)
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.maxFrequency([10,2,3,4,5,5,4,3,2,2], 10), 4)
