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

    def test_case1(self):
        head = create_linked_list([1,2,3,4,5])
        k = 2
        expected = [4,5,1,2,3]
        sol = Solution()
        result = sol.rotateRight(head, k)
        self.assertEqual(linked_list_to_list(result), expected)
    
    def test_case2(self):
        head = create_linked_list([0,1,2])
        k = 4
        expected = [2,0,1]
        sol = Solution()
        result = sol.rotateRight(head, k)
        self.assertEqual(linked_list_to_list(result), expected)
    
    def test_case3(self):
        head = create_linked_list([1])
        k = 0
        expected = [1]
        sol = Solution()
        result = sol.rotateRight(head, k)
        self.assertEqual(linked_list_to_list(result), expected)
