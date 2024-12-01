import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.smallestNumber(5), 7)
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.smallestNumber(10), 15)
    
    def test_case_3(self):
        solution = Solution()
        self.assertEqual(solution.smallestNumber(3), 3)
    
    def test_case_4(self):
        solution = Solution()
        self.assertEqual(solution.smallestNumber(1), 1)
    
    def test_case_5(self):
        solution = Solution()
        self.assertEqual(solution.smallestNumber(1000), 1023)
