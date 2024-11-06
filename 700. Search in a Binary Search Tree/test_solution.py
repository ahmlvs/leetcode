from solution import Solution
from solution import TreeNode
from collections import deque

# Helper function to create a binary tree from a list (level-order)
def list_to_binary_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root

def binary_tree_to_list(root: TreeNode) -> list:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()
    return result


def test_solution():
    solution = Solution()

    # Test 1
    root = list_to_binary_tree([4, 2, 7, 1, 3])
    val = 2
    expected_list = [2, 1, 3]
    assert binary_tree_to_list(solution.searchBST(root, val)) == expected_list

    # Test 2
    root = list_to_binary_tree([4, 2, 7, 1, 3])
    val = 5
    expected_list = []
    assert binary_tree_to_list(solution.searchBST(root, val)) == expected_list

    # Test 3
    root = list_to_binary_tree([1])
    val = 1
    expected_list = [1]
    assert binary_tree_to_list(solution.searchBST(root, val)) == expected_list

    # Test 4
    root = list_to_binary_tree([1, None, 2, None, 3])
    val = 2
    expected_list = [2, None, 3]
    assert binary_tree_to_list(solution.searchBST(root, val)) == expected_list

    print("All tests passed.")


if __name__ == '__main__':
    test_solution()
