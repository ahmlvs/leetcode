import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.reverseBits(43261596), 964176192)
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.reverseBits(4294967293), 3221225471)
    