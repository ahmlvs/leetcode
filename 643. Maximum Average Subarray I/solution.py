# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # max_average = -10**4
        # n = len(nums)

        # for i in range(0, n-k+1):
        #     window_sum = 0
        #     for j in range(k):
        #         window_sum += nums[i+j]
        #     window_average = round(window_sum / k, 5)

        #     if window_average > max_average:
        #         max_average = window_average
        
        # return max_average

        # first get sum for first k el
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            if window_sum > max_sum:
                max_sum = window_sum
        
        return round(max_sum / k, 5)
