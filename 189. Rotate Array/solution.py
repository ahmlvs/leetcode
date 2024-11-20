# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # if k > n
        k = k % n

        # # 1. 2 arrays
        # # copy back to nums
        # nums[:] = nums[-k:] + nums[:-k]
        # # time O(n) and space O(n)

        # # 2. reverse portion of list
        # def reverse(start, end):
        #     while start < end:
        #         nums[start], nums[end] = nums[end], nums[start]

        #         start += 1
        #         end -= 1
        
        # reverse(0, n-1)
        # reverse(0, k-1)
        # reverse(k, n-1)
        # # time O(n) and space O(1)

        # 3. cyclic replacements
        # el counter
        count = 0
        start = 0

        while count < n:
            current = start
            prev_val = nums[start]
            while True:
                # new index
                new_index = (current + k) % n
                # change val for nums and prev
                nums[new_index], prev_val = prev_val, nums[new_index]
                # move current
                current = new_index
                # count update
                count += 1

                # if start == current stop cycle
                if start == current:
                    break
            
            # move to next index
            start += 1
