from solution import Solution, ListNode

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

def test_solution():
    solution = Solution()

    # Test case 1
    head = list_to_linked_list([1,2,3,4,5])
    new_head = solution.reverseList(head)
    assert linked_list_to_list(new_head) == [5,4,3,2,1]

    # Test case 2
    head = list_to_linked_list([1,2])
    new_head = solution.reverseList(head)
    assert linked_list_to_list(new_head) == [2,1]

    # Test case 3
    head = list_to_linked_list([])
    new_head = solution.reverseList(head)
    assert linked_list_to_list(new_head) == []

    print('All tests passed')


if __name__ == '__main__':
    test_solution()
