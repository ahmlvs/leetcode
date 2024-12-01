import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        edges1 = [[0,1],[0,2],[2,3],[2,4]]
        edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
        k = 2
        expected = [9,7,9,8,8]
        self.assertListEqual(Solution().maxTargetNodes(edges1, edges2, k), expected)
    
    def test_case_2(self):
        edges1 = [[0,1],[0,2],[0,3],[0,4]]
        edges2 = [[0,1],[1,2],[2,3]]
        k = 1
        expected = [6,3,3,3,3]
        self.assertListEqual(Solution().maxTargetNodes(edges1, edges2, k), expected)
    