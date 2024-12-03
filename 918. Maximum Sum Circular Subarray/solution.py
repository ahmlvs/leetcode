# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

# Example 1:

# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
# Example 2:

# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
# Example 3:

# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.
 

# Constraints:

# n == nums.length
# 1 <= n <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104

from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # n = len(nums)
        # big_nums = nums + nums
        # max_sum = big_nums[0]

        # for start in range(n):
        #     current_sum = big_nums[start]

        #     for i in range(1, n):
        #         current_sum = max(big_nums[start + i], current_sum + big_nums[start + i])
        #         max_sum = max(max_sum, current_sum)

        # return max_sum
        # TLE

        # idea. total_sum - min_sum is equal to max_circular_sum
        # but if all el < 0 need to get standart max_sum
        n = len(nums)
        total_sum = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        current_max_sum = 0
        current_min_sum = 0

        for i in range(n):
            current_max_sum = max(nums[i], current_max_sum + nums[i])
            max_sum = max(max_sum, current_max_sum)

            current_min_sum = min(nums[i], current_min_sum + nums[i])
            min_sum = min(min_sum, current_min_sum)

            total_sum += nums[i]
        
        circular_sum = total_sum - min_sum

        if circular_sum == 0:
            # return standart max_sum
            return max_sum
        
        return max(max_sum, circular_sum)
