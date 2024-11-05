import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        spells = [5,1,3]
        potions = [1,2,3,4,5]
        success = 7
        self.assertEqual(Solution().successfulPairs(spells, potions, success), [4,0,3])
    
    def test_2(self):
        spells = [3,1,2]
        potions = [8,5,8]
        success = 16
        self.assertEqual(Solution().successfulPairs(spells, potions, success), [2,0,2])
    
    def test_3(self):
        spells = [1,1,1]
        potions = [1,1,1]
        success = 1
        self.assertEqual(Solution().successfulPairs(spells, potions, success), [3,3,3])
