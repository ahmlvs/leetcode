# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # n = len(nums)
        # current_sum = 0
        # min_lenght = float("inf")
        # # left pointer of sliding window
        # left = 0

        # # right pointer
        # for right in range(n):
        #     current_sum += nums[right]

        #     # let's move left to right if more target
        #     while current_sum >= target:
        #         min_lenght = min(min_lenght, right - left + 1)
        #         current_sum -= nums[left]
        #         left += 1

        # return min_lenght if min_lenght != float("inf") else 0

        # for O(nlog(n)) need to use binary search
        def search_j(array, target_el):
            n = len(array)
            left = 0
            right = n - 1

            while left <= right:
                mid = (left + right) // 2

                if array[mid] == target_el:
                    return mid
                elif array[mid] < target_el:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return left


        n = len(nums)

        # prefix sum
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        min_lenght = float("inf")

        # prefix sum sorted
        # so need to find min j
        # prefix_sum[j] - prefix_sum[i] >= target
        for i in range(n):
            target_prefix = prefix_sum[i] + target

            j = search_j(prefix_sum, target_prefix)

            if j <= n:
                # j already with +1
                # because prefix_sum (n+1)
                min_lenght = min(min_lenght, j - i)

        return min_lenght if min_lenght != float("inf") else 0
