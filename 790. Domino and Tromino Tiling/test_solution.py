import unittest
from solution import Solution


class TestResult(unittest.TestCase):
    
    def test_1(self):
        s = Solution()
        self.assertEqual(s.numTilings(3), 5)
    
    def test_2(self):
        s = Solution()
        self.assertEqual(s.numTilings(1), 1)
    
    def test_3(self):
        s = Solution()
        self.assertEqual(s.numTilings(4), 11)
