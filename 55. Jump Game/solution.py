# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105


from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # farthest index we can reach
        farthest = 0

        for j in range(n):
            # if j > farthest we can't reach on it
            # so it is unreachable
            if j > farthest:
                return False
            
            # update farthest
            farthest = max(farthest, j + nums[j])

            # chech if farthest more n-1
            if farthest >= n - 1:
                return True

        return False 
