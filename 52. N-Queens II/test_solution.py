import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(1), 1)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(2), 0)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(3), 0)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(4), 2)
    
    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(5), 10)
    
    def test_case_6(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(6), 4)
    
    def test_case_7(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(7), 40)
    
    def test_case_8(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(8), 92)
    
    def test_case_9(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(9), 352)
    
    def test_case_10(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(10), 724)
    
    def test_case_11(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(11), 2680)
    
    def test_case_12(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(12), 14200)
    
    def test_case_13(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(13), 73712)
