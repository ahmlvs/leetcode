import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_asteroidCollision(self):
        solution = Solution()
        self.assertEqual(solution.asteroidCollision([5,10,-5]), [5,10])
        self.assertEqual(solution.asteroidCollision([8,-8]), [])
        self.assertEqual(solution.asteroidCollision([10,2,-5]), [10])
        self.assertEqual(solution.asteroidCollision([-2,-1,1,2]), [-2,-1,1,2])
        self.assertEqual(solution.asteroidCollision([-2,-2,1,-2]), [-2,-2,-2])
    