import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def text_case_1(self):
        nums = [0,1,1,1,0,0]
        output = 3
        self.assertEqual(Solution.minOperations(nums), output)
    
    def text_case_2(self):
        nums = [0,1,1,1]
        output = -1
        self.assertEqual(Solution.minOperations(nums), output)
