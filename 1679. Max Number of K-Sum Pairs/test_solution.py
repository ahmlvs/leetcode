import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [1,2,3,4]
        k = 5
        self.assertEqual(self.solution.maxOperations(nums, k), 2)
    
    def test_case_2(self):
        nums = [3,1,3,4,3]
        k = 6
        self.assertEqual(self.solution.maxOperations(nums, k), 1)
    
    def test_case_3(self):
        nums = [1,1,1,1]
        k = 2
        self.assertEqual(self.solution.maxOperations(nums, k), 2)
    
    def test_case_4(self):
        nums = [2,2,2,3,1,1,4,1]
        k = 4
        self.assertEqual(self.solution.maxOperations(nums, k), 2)
