import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        expected = [6.0, 0.5, -1.0, 1.0, -1.0]
        result = solution.calcEquation(equations, values, queries)
        self.assertEqual(result, expected)
    
    def test_2(self):
        solution = Solution()
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        expected = [3.75000, 0.40000, 5.00000, 0.20000]
        result = solution.calcEquation(equations, values, queries)
        self.assertEqual(result, expected)
    
    def test_3(self):
        solution = Solution()
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        expected = [0.50000, 2.00000, -1.00000, -1.00000]
        result = solution.calcEquation(equations, values, queries)
        self.assertEqual(result, expected)
