# You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

# For chosen indices i0, i1, ..., ik - 1, your score is defined as:

# The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
# It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
# Return the maximum possible score.

# A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

 

# Example 1:

# Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
# Output: 12
# Explanation: 
# The four possible subsequence scores are:
# - We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
# - We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
# - We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
# - We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
# Therefore, we return the max score, which is 12.
# Example 2:

# Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
# Output: 30
# Explanation: 
# Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.
 

# Constraints:

# n == nums1.length == nums2.length
# 1 <= n <= 105
# 0 <= nums1[i], nums2[j] <= 105
# 1 <= k <= n

from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # combine nums1 and nums2 with their indices 
        # and sort by nums2 in descending order
        combined = sorted(zip(nums2, nums1), reverse=True)

        # heap for nums1_k
        heap = []
        # and sum for nums1_k
        sum_heap = 0
        max_score = 0

        # on each step n2 -> desc
        for n2, n1 in combined:
            # add n1 in heap
            heapq.heappush(heap, n1)
            # update sum
            sum_heap += n1

            # check if len_heap <= k
            if len(heap) > k:
                # delete smallest element
                # and update heap sum
                sum_heap -= heapq.heappop(heap)
            
            # if len_heap == k
            # update max_score
            if len(heap) == k:
                # n2 every step decreasing, so on each step we have
                # min(n2)
                max_score = max(max_score, n2 * sum_heap)
            
        return max_score
