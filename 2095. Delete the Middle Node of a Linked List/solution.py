# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

# Example 1:


# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node. 
# Example 2:


# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.
# Example 3:


# Input: head = [2,1]
# Output: [2]
# Explanation:
# The above figure represents the given linked list.
# For n = 2, node 1 with value 1 is the middle node, which is marked in red.
# Node 0 with value 2 is the only node remaining after removing node 1.
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 1 <= Node.val <= 105

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # n = 1
        # node = head
        
        # while node.next:
        #     n += 1
        #     node = node.next
        
        # mid_el_index = n // 2
        # if mid_el_index == 0:
        #     return None

        # k = 0
        # mid_minus_one = None
        # node = head

        # while k < mid_el_index:
        #     mid_minus_one = node
        #     node = node.next
        #     k += 1
        
        # mid_minus_one.next = node.next

        # return head

        ## fast ans slow pointer approuch

        # if no nodes or only one node in head return None
        if head is None or head.next is None:
            return None

        # fast = 2 * slow
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            # move to next node
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # when fast finish, slow in the middle
        # remove middle
        prev.next = slow.next

        return head
