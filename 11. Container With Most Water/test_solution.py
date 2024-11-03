import unittest
from solution import Solution

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.maxArea([1,8,6,2,5,4,8,3,7]), 49)

    def test_case_2(self):
        self.assertEqual(self.solution.maxArea([1,1]), 1)
    
    def test_case_3(self):
        self.assertEqual(self.solution.maxArea([4,3,100,100,4]), 100)
