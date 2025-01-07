import unittest
from solution import Solution, ListNode


class TestSolution(unittest.TestCase):
    
    def test_case_1(self):
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        expected = [1, 1, 2, 3, 4, 4, 5, 6]
        result = Solution().mergeKLists([ListNode.from_list(l) for l in lists])
        self.assertEqual(result.to_list() if result else [], expected)

    def test_case_2(self):
        lists = []
        expected = []
        result = Solution().mergeKLists([ListNode.from_list(l) for l in lists])
        self.assertEqual(result.to_list() if result else [], expected)

    def test_case_3(self):
        lists = [[]]
        expected = []
        result = Solution().mergeKLists([ListNode.from_list(l) for l in lists])
        self.assertEqual(result.to_list() if result else [], expected)
