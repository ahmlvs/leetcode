import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.findKthLargest([3,2,1,5,6,4], 2), 5)
    
    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)
