import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        code = [5,7,1,4]
        k = 3
        expected_result = [12,10,16,13]
        solution = Solution()
        self.assertListEqual(solution.decrypt(code, k), expected_result)
    
    def test_case_2(self):
        code = [1,2,3,4]
        k = 0
        expected_result = [0,0,0,0]
        solution = Solution()
        self.assertListEqual(solution.decrypt(code, k), expected_result)
    
    def test_case_3(self):
        code = [2,4,9,3]
        k = -2
        expected_result = [12,5,6,13]
        solution = Solution()
        self.assertListEqual(solution.decrypt(code, k), expected_result)
    