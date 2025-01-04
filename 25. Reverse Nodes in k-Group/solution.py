# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
 

# Follow-up: Can you solve the problem in O(1) extra memory space?

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# help func to reverse group
def reverse(start, end):
    prev, curr = None, start
    while curr != end:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # dummy for edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            # check if we have k node more
            kth_node = prev_group_end
            for _ in range(k):
                kth_node = kth_node.next
                # if None we don't have k nodes
                if not kth_node:
                    return dummy.next
            
            # define start and end for next group
            group_start = prev_group_end.next
            group_end = kth_node.next

            # reverse
            reverse(group_start, group_end)

            # re-link
            prev_group_end.next = kth_node
            group_start.next = group_end

            # move
            prev_group_end = group_start
