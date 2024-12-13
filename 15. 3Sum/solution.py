# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # sort nums
        nums_sorted = sorted(nums)
        result = []

        # fix one and whith 2 pointers wind another 2
        for i in range(n-2):
            # check duplicates
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                # move to next
                continue
            
            # let's find 2 another els
            left, right = i+1, n-1
            while left < right:
                total = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]

                if total == 0:
                    result.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])

                    # check for duplicates for left
                    while left < right and nums_sorted[left] == nums_sorted[left+1]:
                        left += 1
                    
                    # check for duplicates for right
                    while left < right and nums_sorted[right] == nums_sorted[right-1]:
                        right -= 1
                    
                    # move pointers
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
            
        return result    
