import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.kidsWithCandies([2,3,5,1,3], 3), [True,True,True,False,True])
    
    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.kidsWithCandies([4,2,1,1,2], 1), [True,False,False,False,False])
    
    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.kidsWithCandies([12,1,12], 10), [True,False,True])
