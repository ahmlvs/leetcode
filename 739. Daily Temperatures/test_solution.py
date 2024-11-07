import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.dailyTemperatures([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
    
    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.dailyTemperatures([30,40,50,60]), [1,1,1,0])
    
    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.dailyTemperatures([30,60,90]), [1,1,0])
    