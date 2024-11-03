import unittest
from solution import Solution

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [1,2,3,4,5]
        self.assertEqual(self.solution.increasingTriplet(nums), True)
    
    def test_case_2(self):
        nums = [5,4,3,2,1]
        self.assertEqual(self.solution.increasingTriplet(nums), False)
    
    def test_case_3(self):
        nums = [2,1,5,0,4,6]
        self.assertEqual(self.solution.increasingTriplet(nums), True)
    
    def test_case_4(self):
        nums = [1,1,1,1,1]
        self.assertEqual(self.solution.increasingTriplet(nums), False)
    
    def test_case_5(self):
        nums = [20,100,10,12,5,13]
        self.assertEqual(self.solution.increasingTriplet(nums), True)
