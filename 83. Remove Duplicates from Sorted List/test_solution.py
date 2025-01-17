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
        head = create_linked_list([1,1,2])
        expected = [1,2]
        solution = Solution().deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(solution), expected)
    
    def test_case_2(self):
        head = create_linked_list([1,1,2,3,3])
        expected = [1,2,3]
        solution = Solution().deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(solution), expected)
    
    def test_case_3(self):
        head = create_linked_list([])
        expected = []
        solution = Solution().deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(solution), expected)
    
    def test_case_4(self):
        head = create_linked_list([1,1,1,1,1])
        expected = [1]
        solution = Solution().deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(solution), expected)
