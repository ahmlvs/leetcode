import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        expected = 1
        s = Solution()
        self.assertEqual(s.numIslands(grid), expected)
    
    def test_case_2(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        expected = 3
        s = Solution()
        self.assertEqual(s.numIslands(grid), expected)
