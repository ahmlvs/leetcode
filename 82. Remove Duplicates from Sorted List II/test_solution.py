import unittest
from solution import ListNode, Solution

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a Python list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        head = create_linked_list([1,2,3,3,4,4,5])
        expected = [1,2,5]
        output = Solution().deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(output), expected)
    
    def test_case_2(self):
        head = create_linked_list([1,1,1,2,3])
        expected = [2,3]
        output = Solution().deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(output), expected)

    def test_case_3(self):
        head = create_linked_list([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
        expected = []
        output = Solution().deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(output), expected)
