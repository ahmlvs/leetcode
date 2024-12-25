# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if k==0 or head has 1 el -> return head
        if not head or not head.next or k == 0:
            return head
        
        # need to find list len
        n = 1
        current = head
        while current.next:
            current = current.next
            n += 1
        
        # calc real k
        k = k % n

        if k == 0:
            return head
        
        # make list circular
        current.next = head

        # calc number for new tail after rotation
        rotate = n - k #times
        new_tail = head
        # 1, 2, ..., rotate - 1
        for _ in range(1, rotate):
            print(new_tail.val)
            new_tail = new_tail.next
        
        # set new head
        new_head = new_tail.next
        # break circle
        new_tail.next = None

        return new_head
        