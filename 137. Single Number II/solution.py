# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each element in nums appears exactly three times except for one element which appears once.

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR ^
        # a ^ a = 0 
	    # a ^ 0 = a 

        unique_element = 0
        not_unique_element = 0
        
        for num in nums:
            unique_element = (unique_element ^ num) & ~not_unique_element
            not_unique_element = (not_unique_element ^ num) & ~unique_element
        
        return unique_element
