import unittest
from solution import Solution, ListNode

def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        head = list_to_linked_list([3, 2, 0, -4])
        pos = 1
        head.next.next.next.next = head.next
        self.assertTrue(sol.hasCycle(head))
    
    def test_case_2(self):
        sol = Solution()
        head = list_to_linked_list([1, 2])
        pos = 0
        head.next.next = head
        self.assertTrue(sol.hasCycle(head))
    
    def test_case_3(self):
        sol = Solution()
        head = list_to_linked_list([1])
        pos = -1
        self.assertFalse(sol.hasCycle(head))
    