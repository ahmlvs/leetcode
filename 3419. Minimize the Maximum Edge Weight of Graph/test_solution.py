import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        n = 5
        edges = [[1,0,1],[2,0,2],[3,0,1],[4,3,1],[2,1,1]]
        threshold = 2
        self.assertEqual(Solution().minMaxWeight(n, edges, threshold), 1)
    
    def test_case_2(self):
        n = 5
        edges = [[0,1,1],[0,2,2],[0,3,1],[0,4,1],[1,2,1],[1,4,1]]
        threshold = 1
        self.assertEqual(Solution().minMaxWeight(n, edges, threshold), -1)
    
    def test_case_3(self):
        n = 5
        edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[3,4,2],[4,0,1]]
        threshold = 1
        self.assertEqual(Solution().minMaxWeight(n, edges, threshold), 2)
    
    def test_case_4(self):
        n = 5
        edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[4,0,1]]
        threshold = 1
        self.assertEqual(Solution().minMaxWeight(n, edges, threshold), -1)
    
    def test_case_5(self):
        n = 4
        edges = [[2,0,39],[2,1,72],[2,3,67],[1,2,78],[3,0,10],[0,2,81]]
        threshold = 2
        self.assertEqual(Solution().minMaxWeight(n, edges, threshold), 78)
    
    def test_case_6(self):
        n = 6
        edges = [[0,4,26],[4,3,68],[1,0,84],[0,1,22],[1,2,82],[0,3,78],[5,0,86],[1,3,70],[3,1,43],[4,2,61],[2,4,13],[5,4,38]]
        threshold = 1
        self.assertEqual(Solution().minMaxWeight(n, edges, threshold), 84)
