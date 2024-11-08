import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]), 2)
    
    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]), 4)
    
    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]), 2)
