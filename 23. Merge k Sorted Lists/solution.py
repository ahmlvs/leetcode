# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

from typing import List, Optional
from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Utility to create a linked list from a list
    @staticmethod
    def from_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Utility to convert a linked list to a list
    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # nin-heap (node val, index of list, node)
        heap = []

        # push head nodes to heap
        for i, l in enumerate(lists):
            if l:
                heappush(heap, (l.val, i, l))
        
        # dummy to for edge cases
        dummy = ListNode()
        curr = dummy

        # link all nodes in heap
        while heap:
            val, i, node = heappop(heap)
            curr.next = node
            curr = curr.next
            # add next nodes
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
            
        return dummy.next
