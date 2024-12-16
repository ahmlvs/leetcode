import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.combine(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.combine(1, 1), [[1]])
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.combine(4, 1), [[1], [2], [3], [4]])
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.combine(3, 3), [[1, 2, 3]])


if __name__ == '__main__':
    t = TestSolution()
    t.test_case_1()
