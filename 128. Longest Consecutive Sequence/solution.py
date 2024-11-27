# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n
        
        # set to check el for O(1)
        nums_set = set(nums)
        max_sequence = 0

        for num in nums_set:
            # if no num - 1
            # num is start of sequence
            if num - 1 not in nums_set:
                current_num = num
                current_sequence = 1

                # check all sequence
                while current_num + 1 in nums_set:
                    current_sequence += 1
                    current_num += 1
                
                max_sequence = max(max_sequence, current_sequence)

        return max_sequence
