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
    def test_1(self):
        solution = Solution()
        head = list_to_linked_list([1,2,3,4,5])
        expected = [1,3,5,2,4]
        actual = linked_list_to_list(solution.oddEvenList(head))
        self.assertEqual(expected, actual)
    
    def test_2(self):
        solution = Solution()
        head = list_to_linked_list([2,1,3,5,6,4,7])
        expected = [2,3,6,7,1,5,4]
        actual = linked_list_to_list(solution.oddEvenList(head))
        self.assertEqual(expected, actual)
