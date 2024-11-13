import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_isHappy_1(self):
        solution = Solution()
        self.assertEqual(solution.isHappy(19), True)
    
    def test_isHappy_2(self):
        solution = Solution()
        self.assertEqual(solution.isHappy(2), False)
    
    def test_isHappy_3(self):
        solution = Solution()
        self.assertEqual(solution.isHappy(1), True)
    
    def test_isHappy_4(self):
        solution = Solution()
        self.assertEqual(solution.isHappy(1112324244), False)
    