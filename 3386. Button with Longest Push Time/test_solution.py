import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        events = [[1, 2], [2, 5], [3, 9], [1, 15]]
        expected_result = 1
        solution = Solution()
        self.assertEqual(solution.buttonWithLongestTime(events), expected_result)
    
    def test_case_2(self):
        events = [[10, 5], [1, 7]]
        expected_result = 10
        solution = Solution()
        self.assertEqual(solution.buttonWithLongestTime(events), expected_result)
