# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
 

# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)

        # dp = [1] * n

        # # O(n^2) check all els j before each element i
        # # and if val_j < val_i
        # # it means i next el it LIS
        # for i in range(n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             # we need to find longest for all j's
        #             dp[i] = max(dp[i], dp[j] + 1)
        
        # return max(dp)

        # O(n log(n)) need to use binary search
        # to find smallest el in sorted array
        def custom_bisect_left(arr, target):
            left, right = 0, len(arr)

            while left < right:
                mid = (left + right) // 2

                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            
            return left
        
        subsequence = []

        for num in nums:
            # find ind to place num in subsequence
            i = custom_bisect_left(subsequence, num)
            # if i in subsequence
            # relplace i_val with num
            # or append in right
            if i < len(subsequence):
                subsequence[i] = num
            else:
                subsequence.append(num)
        
        return len(subsequence)
