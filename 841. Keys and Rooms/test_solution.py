import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        rooms = [[1],[2],[3],[]]
        expected = True
        self.assertEqual(Solution().canVisitAllRooms(rooms), expected)
    
    def test_2(self):
        rooms = [[1,3],[3,0,1],[2],[0]]
        expected = False
        self.assertEqual(Solution().canVisitAllRooms(rooms), expected)
    
    def test_3(self):
        rooms = [[1],[1],[1],[1],[]]
        expected = False
        self.assertEqual(Solution().canVisitAllRooms(rooms), expected)
