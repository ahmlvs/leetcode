import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        numberOfUsers = 2
        events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]
        output = [2,2]
        self.assertEqual(Solution().countMentions(numberOfUsers, events), output)
    
    def test_case_2(self):
        numberOfUsers = 2
        events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]
        output = [2,2]
        self.assertEqual(Solution().countMentions(numberOfUsers, events), output)
    
    def test_case_3(self):
        numberOfUsers = 2
        events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]
        output = [0,1]
        self.assertEqual(Solution().countMentions(numberOfUsers, events), output)
