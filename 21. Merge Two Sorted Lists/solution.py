# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if not list1:
        #     return list2
        # elif not list2:
        #     return list1
        
        # # set result head
        # if list1.val <= list2.val:
        #     result = list1
        #     list1 = list1.next
        # else:
        #     result = list2
        #     list2 = list2.next
        
        # # result will be changed over loop
        # output = result

        # # add next nodes
        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         result.next = list1
        #         list1 = list1.next
        #     else:
        #         result.next = list2
        #         list2 = list2.next
        #     result = result.next
        
        # # add final nodes
        # if list1:
        #     result.next = list1
        # elif list2:
        #     result.next = list2
        
        # return output

        ## dummy node for edge cases
        dummy = ListNode(-1)
        current = dummy

        # add next nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # add final nodes
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # our head is dummy next
        return dummy.next
        