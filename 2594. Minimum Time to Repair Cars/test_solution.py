import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        ranks = [4,2,3,1]
        cars = 10
        expected = 16
        self.assertEqual(solution.repairCars(ranks, cars), expected)
    
    def test_case_2(self):
        solution = Solution()
        ranks = [5,1,8]
        cars = 6
        expected = 16
        self.assertEqual(solution.repairCars(ranks, cars), expected)
