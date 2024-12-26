# Given the head of a linked list, return the list after sorting it in ascending order.

 

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105
 

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_mid(head: Optional[ListNode]):
    # 2 pointers
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(l1: Optional[ListNode], l2: Optional[ListNode]):
    # dummy for edge cases
    dummy = ListNode()
    tail = dummy

    # connect smallest to tail
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    # connect remaining nodes
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    
    return dummy.next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if no nodes or only 1 -- already sorted
        if not head or not head.next:
            return head
        
        # idea to divide list in 2
        # and req sort them
        mid = get_mid(head)
        left = head
        right = mid.next
        # break list 2 halves
        mid.next = None

        # sort them
        left = self.sortList(left)
        right = self.sortList(right)

        # merge 2 lists
        return merge(left, right)
