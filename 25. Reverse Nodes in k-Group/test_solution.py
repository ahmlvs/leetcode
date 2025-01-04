import unittest
from solution import ListNode, Solution

# help func to convert list to linked list
def list_to_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# help func to convert linked list to list
def linked_list_to_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


class TestSolution(unittest.TestCase):

    def test_case1(self):
        head = list_to_linked_list([1,2,3,4,5])
        k = 2
        expected = [2,1,4,3,5]
        s = Solution().reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(s), expected)
    
    def test_case2(self):
        head = list_to_linked_list([1,2,3,4,5])
        k = 3
        expected = [3,2,1,4,5]
        s = Solution().reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(s), expected)
