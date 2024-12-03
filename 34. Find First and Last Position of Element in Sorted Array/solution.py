# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        # func to find taget ind
        def found_bound(is_first):
            n = len(nums)
            left = 0
            right = n - 1
            bound = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    # save ind
                    bound = mid

                    # and continiue search
                    if is_first:
                        # search in left side
                        right = mid - 1
                    else:
                        # search in right side
                        left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return bound
        
        first = found_bound(True)
        if first == -1:
            # not found target
            return [-1, -1]
        
        last = found_bound(False)

        return [first, last]
