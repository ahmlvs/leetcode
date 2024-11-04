import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')
    
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        self.solution = Solution()
        print('setUp')
    
    def tearDown(self):
        print('tearDown')

    def test_asteroidCollision(self):
        print('test_asteroidCollision')
        self.assertEqual(self.solution.asteroidCollision([5,10,-5]), [5,10])
        self.assertEqual(self.solution.asteroidCollision([8,-8]), [])
        self.assertEqual(self.solution.asteroidCollision([10,2,-5]), [10])
        self.assertEqual(self.solution.asteroidCollision([-2,-1,1,2]), [-2,-1,1,2])
        self.assertEqual(self.solution.asteroidCollision([-2,-2,1,-2]), [-2,-2,-2])


if __name__ == '__main__':
    unittest.main()
    