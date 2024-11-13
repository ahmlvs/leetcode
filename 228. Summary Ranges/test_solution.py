import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertListEqual(sol.summaryRanges([0,1,2,4,5,7]), ["0->2","4->5","7"])
    
    def test_case_2(self):
        sol = Solution()
        self.assertListEqual(sol.summaryRanges([0,2,3,4,6,8,9]), ["0","2->4","6","8->9"])

    def test_case_3(self):
        sol = Solution()
        self.assertListEqual(sol.summaryRanges([]), [])
    
    def test_case_4(self):
        sol = Solution()
        self.assertListEqual(sol.summaryRanges([0,2,3,4,6,8,9,100]), ["0","2->4","6","8->9","100"])
        