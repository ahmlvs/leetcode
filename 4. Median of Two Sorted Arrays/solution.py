# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # # 1. variant
        # # merge and sort O((m + n)log(m + n))
        # merged = nums1 + nums2
        # merged.sort()

        # n = len(merged)
        # if n % 2 == 1:
        #     return merged[n // 2]
        # else:
        #     return (merged[n // 2 - 1] + merged[n // 2]) / 2
        
        # 2. variant
        # binary search for partition

        # small array for BS
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        # for nums1
        low, high = 0, x

        while low <= high:
            partition_x = (low + high) // 2
            partition_y = (x + y + 1) // 2 - partition_x

            # max for left and min for right parts
            # if partition_x == 0 nothing in left part
            max_left_x = float("-inf") if partition_x == 0 else nums1[partition_x - 1]
            # if partition_x == x nothing in right part
            min_right_x = float("inf") if partition_x == x else nums1[partition_x]

            max_left_y = float("-inf") if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float("inf") if partition_y == y else nums2[partition_y]

            # check if correct
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # found correct partition
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                # move left in nums1
                high = partition_x - 1
            else:
                # move right in nums1
                low = partition_x + 1
        
        # if nums1 and nums2 not sorted
        return -1
