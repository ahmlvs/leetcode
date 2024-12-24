import unittest
from solution import Solution, Node

def list_to_array(head):
    """Helper method to convert a linked list to an array representation for validation."""
    nodes = []
    mapping = {}
    current = head
    index = 0
    
    while current:
        mapping[current] = index
        nodes.append([current.val, None])
        current = current.next
        index += 1
    
    current = head
    index = 0
    while current:
        if current.random:
            nodes[index][1] = mapping[current.random]
        index += 1
        current = current.next
    return nodes

def array_to_list(array):
    """Helper method to convert an array representation into a linked list."""
    if not array:
        return None
    nodes = [Node(val) for val, _ in array]
    for i, (_, random_index) in enumerate(array):
        if i < len(array) - 1:
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    return nodes[0]



class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = Solution()
        head = array_to_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
        copied_head = s.copyRandomList(head)
        self.assertEqual(list_to_array(copied_head), [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])

    def test_case_2(self):
        s = Solution()
        head = array_to_list([[1, 1], [2, 1]])
        copied_head = s.copyRandomList(head)
        self.assertEqual(list_to_array(copied_head), [[1, 1], [2, 1]])

    def test_case_3(self):
        s = Solution()
        head = array_to_list([[3, None], [3, 0], [3, None]])
        copied_head = s.copyRandomList(head)
        self.assertEqual(list_to_array(copied_head), [[3, None], [3, 0], [3, None]])

    def test_empty_list(self):
        s = Solution()
        head = array_to_list([])
        copied_head = s.copyRandomList(head)
        self.assertIsNone(copied_head)

    def test_single_node(self):
        s = Solution()
        head = array_to_list([[1, None]])
        copied_head = s.copyRandomList(head)
        self.assertEqual(list_to_array(copied_head), [[1, None]])

    def test_single_node_with_random(self):
        s = Solution()
        head = array_to_list([[1, 0]])
        copied_head = s.copyRandomList(head)
        self.assertEqual(list_to_array(copied_head), [[1, 0]])
