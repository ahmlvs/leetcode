import unittest
from solution import Node, Solution


# help func to build tree
def build_tree(values):
    if not values:
        return None
    nodes = [Node(val) if val is not None else None for val in values]
    for i in range(len(nodes)):
        if nodes[i] is not None:
            if 2 * i + 1 < len(nodes):
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nodes):
                nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

# help func to convert tree to list with next pointers
def to_next_list(root):
    if not root:
        return []
    result = []
    current = root
    while current:
        level = []
        node = current
        while node:
            level.append(node.val)
            node = node.next
        result.extend(level + ['#'])
        current = current.left
    return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        connected_root = self.solution.connect(root)
        self.assertEqual(to_next_list(connected_root), [1, '#', 2, 3, '#', 4, 5, 6, 7, '#'])

    def test_empty_tree(self):
        root = build_tree([])
        connected_root = self.solution.connect(root)
        self.assertEqual(to_next_list(connected_root), [])

    def test_single_node(self):
        root = build_tree([1])
        connected_root = self.solution.connect(root)
        self.assertEqual(to_next_list(connected_root), [1, '#'])

    def test_two_levels(self):
        root = build_tree([1, 2, 3])
        connected_root = self.solution.connect(root)
        self.assertEqual(to_next_list(connected_root), [1, '#', 2, 3, '#'])


if __name__ == '__main__':
    unittest.main()
