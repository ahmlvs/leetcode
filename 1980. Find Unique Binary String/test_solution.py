import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertIn(solution.findDifferentBinaryString(["01", "10"]), ["00", "11"])
    
    def test_case_2(self):
        solution = Solution()
        self.assertIn(solution.findDifferentBinaryString(["00", "01"]), ["10", "11"])
    
    def test_case_3(self):
        solution = Solution()
        self.assertIn(solution.findDifferentBinaryString(["111", "011", "001"]), ["000", "010", "100", "110", "101"])
