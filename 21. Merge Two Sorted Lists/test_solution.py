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
        list1 = list_to_linked_list([1, 2, 4])
        list2 = list_to_linked_list([1, 3, 4])
        expected = [1, 1, 2, 3, 4, 4]
        output = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(expected, linked_list_to_list(output))
    
    def test_case_2(self):
        list1 = list_to_linked_list([])
        list2 = list_to_linked_list([])
        expected = []
        output = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(expected, linked_list_to_list(output))
    
    def test_case_3(self):
        list1 = list_to_linked_list([])
        list2 = list_to_linked_list([0])
        expected = [0]
        output = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(expected, linked_list_to_list(output))
    
    def test_case_4(self):
        list1 = list_to_linked_list([1, 2, 4])
        list2 = list_to_linked_list([1, 3, 4, 5])
        expected = [1, 1, 2, 3, 4, 4, 5]
        output = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(expected, linked_list_to_list(output))
        