import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.findPeakElement([1,2,3,1]), 2)
    
    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.findPeakElement([1,2,1,3,5,6,4]), 5)
    
    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.findPeakElement([1]), 0)
    
    def test_4(self):
        solution = Solution()
        self.assertEqual(solution.findPeakElement([1,2,3,1,0,-1,-2,-3,-4,-5]), 2)
