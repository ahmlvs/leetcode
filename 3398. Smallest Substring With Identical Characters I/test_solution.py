import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "000001"
        numOps = 1

        expected = 2
        self.assertEqual(sol.minLength(s, numOps), expected)
    
    def test_case_2(self):
        sol = Solution()
        s = "0000"
        numOps = 2

        expected = 1
        self.assertEqual(sol.minLength(s, numOps), expected)
    
    def test_case_3(self):
        sol = Solution()
        s = "0101"
        numOps = 0

        expected = 1
        self.assertEqual(sol.minLength(s, numOps), expected)
    
    def test_case_4(self):
        sol = Solution()
        s = "1101"
        numOps = 1

        expected = 1
        self.assertEqual(sol.minLength(s, numOps), expected)
