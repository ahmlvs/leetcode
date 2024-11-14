import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_mySqrt_1(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(4), 2)
    
    def test_mySqrt_2(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(8), 2)
    
    def test_mySqrt_3(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(1), 1)
    
    def test_mySqrt_4(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(0), 0)
    
    def test_mySqrt_5(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(64), 8)
    
    def test_mySqrt_6(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(65), 8)
    
    def test_mySqrt_7(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(63), 7)
