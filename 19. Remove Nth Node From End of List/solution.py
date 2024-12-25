# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy for edge cases
        dummy = ListNode(0)
        dummy.next = head

        # 2 pointers
        first = dummy
        second = dummy

        # move first n+1 steps ahead
        for _ in range(n+1):
            first = first.next
        
        # based on ex1
        # now first is 3, second 0
        # let's move first till end, with second
        while first:
            first = first.next
            second = second.next

        # based on ex1
        # now first is None (after 5), second 3
        # and need to delete 4
        second.next = second.next.next

        return dummy.next
