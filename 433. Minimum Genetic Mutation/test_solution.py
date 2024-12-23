import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = ["AACCGGTA"]
        expected = 1
        s = Solution()
        self.assertEqual(s.minMutation(startGene, endGene, bank), expected)
    
    def test_case_2(self):
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
        expected = 2
        s = Solution()
        self.assertEqual(s.minMutation(startGene, endGene, bank), expected)
    
    def test_case_3(self):
        startGene = "AAAAACCC"
        endGene = "AACCCCCC"
        bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
        expected = 3
        s = Solution()
        self.assertEqual(s.minMutation(startGene, endGene, bank), expected)
    
    def test_case_4(self):
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = []
        expected = -1
        s = Solution()
        self.assertEqual(s.minMutation(startGene, endGene, bank), expected)
