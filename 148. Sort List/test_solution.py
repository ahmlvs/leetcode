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
        s = Solution()
        head = create_linked_list([4,2,1,3])
        expected = [1,2,3,4]
        self.assertEqual(linked_list_to_list(s.sortList(head)), expected)
    
    def test_case_2(self):
        s = Solution()
        head = create_linked_list([-1,5,3,4,0])
        expected = [-1,0,3,4,5]
        self.assertEqual(linked_list_to_list(s.sortList(head)), expected)
    
    def test_case_3(self):
        s = Solution()
        head = create_linked_list([])
        expected = []
        self.assertEqual(linked_list_to_list(s.sortList(head)), expected)
