import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        n = 6
        connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
        expected_result = 3
        solution = Solution()
        self.assertEqual(solution.minReorder(n, connections), expected_result)
    
    def test_case_2(self):
        n = 5
        connections = [[1,0],[1,2],[3,2],[3,4]]
        expected_result = 2
        solution = Solution()
        self.assertEqual(solution.minReorder(n, connections), expected_result)
    
    def test_case_3(self):
        n = 3
        connections = [[1,0],[2,0]]
        expected_result = 0
        solution = Solution()
        self.assertEqual(solution.minReorder(n, connections), expected_result)
    
    def test_case_4(self):
        n = 3
        connections = [[1,2],[2,0]]
        expected_result = 0
        solution = Solution()
        self.assertEqual(solution.minReorder(n, connections), expected_result)
    
    def test_case_5(self):
        n = 6
        connections = [[0,2],[0,3],[4,1],[4,5],[5,0]]
        expected_result = 3
        solution = Solution()
        self.assertEqual(solution.minReorder(n, connections), expected_result)
