import unittest
from solution import Solution, ListNode

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
        head = create_linked_list([1,2,3,4,5])
        left = 2
        right = 4
        expected_result = [1,4,3,2,5]
        solution = Solution()
        result = solution.reverseBetween(head, left, right)
        self.assertEqual(linked_list_to_list(result), expected_result)
    
    def test_case_2(self):
        head = create_linked_list([5])
        left = 1
        right = 1
        expected_result = [5]
        solution = Solution()
        result = solution.reverseBetween(head, left, right)
        self.assertEqual(linked_list_to_list(result), expected_result)
