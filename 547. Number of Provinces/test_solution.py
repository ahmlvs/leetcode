import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        expected_result = 2
        solution = Solution()
        self.assertEqual(solution.findCircleNum(isConnected), expected_result)
    
    def test_case_2(self):
        isConnected = [[1,0,0],[0,1,0],[0,0,1]]
        expected_result = 3
        solution = Solution()
        self.assertEqual(solution.findCircleNum(isConnected), expected_result)
    
    def test_case_3(self):
        isConnected = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        expected_result = 4
        solution = Solution()
        self.assertEqual(solution.findCircleNum(isConnected), expected_result)
