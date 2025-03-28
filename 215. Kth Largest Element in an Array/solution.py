# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # init mip heap from first k el
        heap = nums[:k]
        # creates a min-heap in O(k)
        heapq.heapify(heap)

        for num in nums[k:]:
            # if num > smallest heap el -- change it
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        # root is the smallest in k el
        return heap[0]
