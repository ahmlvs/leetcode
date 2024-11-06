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
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        head = list_to_linked_list([1,3,4,7,1,2,6])
        head = solution.deleteMiddle(head)
        self.assertEqual(linked_list_to_list(head), [1,3,4,1,2,6])
    
    def test_case_2(self):
        solution = Solution()
        head = list_to_linked_list([1,2,3,4])
        head = solution.deleteMiddle(head)
        self.assertEqual(linked_list_to_list(head), [1,2,4])
    
    def test_case_3(self):
        solution = Solution()
        head = list_to_linked_list([2,1])
        head = solution.deleteMiddle(head)
        self.assertEqual(linked_list_to_list(head), [2])
    
    def test_case_4(self):
        solution = Solution()
        head = list_to_linked_list([1])
        head = solution.deleteMiddle(head)
        self.assertEqual(linked_list_to_list(head), [])
