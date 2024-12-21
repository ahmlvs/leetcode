import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = [0, 1]
        solution = Solution()
        self.assertListEqual(solution.findOrder(numCourses, prerequisites), expected)

    def test_case_2(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        expected = [0, 1, 2, 3]
        solution = Solution()
        self.assertListEqual(solution.findOrder(numCourses, prerequisites), expected)

    def test_case_3(self):
        numCourses = 1
        prerequisites = []
        expected = [0]
        solution = Solution()
        self.assertListEqual(solution.findOrder(numCourses, prerequisites), expected)

    def test_case_4(self):
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        expected = []
        solution = Solution()
        self.assertListEqual(solution.findOrder(numCourses, prerequisites), expected)
