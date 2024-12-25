# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
 

# Follow up: Could you do it in one pass?

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # dummy for edge cases like left == 1
        dummy = ListNode(0)
        dummy.next = head

        # init prev and more to left-1
        prev = dummy
        for _ in range(left-1):
            prev = prev.next
        
        # reverse sublist
        current = prev.next # left
        next_node = None # temporaly
        for _ in range(right - left + 1):
            tmp = current.next # to move then current
            current.next = next_node
            next_node = current 
            current = tmp
        
        # connect sublist to list
        # based on ex.1
        # prev = 1, current = 5, next_node = 4
        # and prev next is 2 
        prev.next.next = current
        prev.next = next_node

        return dummy.next
