import unittest
from solution import ListNode, Solution

def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        l1 = list_to_linked_list([2, 4, 3])
        l2 = list_to_linked_list([5, 6, 4])
        expected = [7, 0, 8]
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), expected)
    
    def test_case_2(self):
        l1 = list_to_linked_list([0])
        l2 = list_to_linked_list([0])
        expected = [0]
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), expected)
    
    def test_case_3(self):
        l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = list_to_linked_list([9, 9, 9, 9])
        expected = [8, 9, 9, 9, 0, 0, 0, 1]
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), expected)
