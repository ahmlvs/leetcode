import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = True
        self.assertEqual(Solution().canFinish(numCourses, prerequisites), expected)
    
    def test_case_2(self):
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        expected = False
        self.assertEqual(Solution().canFinish(numCourses, prerequisites), expected)
