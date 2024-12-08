import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.constructTransformedArray([3,-2,1,1]), [1,1,1,3])
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.constructTransformedArray([-1,4,-1]), [-1,-1,4])
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.constructTransformedArray([0,0,0,0]), [0,0,0,0])
