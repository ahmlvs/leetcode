import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.areAlmostEqual("bank", "kanb"), True)
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.areAlmostEqual("attack", "defend"), False)
    
    def test_case_3(self):
        solution = Solution()
        self.assertEqual(solution.areAlmostEqual("kelb", "kelb"), True)
