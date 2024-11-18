import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        result = solution.addBinary("11", "1")
        self.assertEqual(result, "100")
    
    def test_case_2(self):
        solution = Solution()
        result = solution.addBinary("1010", "1011")
        self.assertEqual(result, "10101")
    
    def test_case_3(self):
        solution = Solution()
        result = solution.addBinary("1", "1")
        self.assertEqual(result, "10")
    
    def test_case_4(self):
        solution = Solution()
        result = solution.addBinary("0", "0")
        self.assertEqual(result, "0")
    