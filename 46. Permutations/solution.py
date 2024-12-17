# Given an array nums of distinct integers, return all the possible 
# permutations
# . You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def backtrack(path, used):
            print(path, used)
            if len(path) == n:
                # add copy of path to result
                result.append(path[:])
            
            for i in range(n):
                # if true skip
                if used[i]:
                    continue

                # add this el to path
                path.append(nums[i])
                used[i] = True

                backtrack(path, used)

                # back this el from path
                path.pop()
                used[i] = False
        
        used = [False] * n
        backtrack([], used)
        return result
        
        ## use only nums
        # n = len(nums)
        # result = []

        # def backtrack(start):
        #     # print(start, result)
        #     if start == n:
        #         result.append(nums[:])
            
        #     for i in range(start, n):
        #         # swap
        #         nums[start], nums[i] = nums[i], nums[start]
        #         # next level
        #         backtrack(start+1)
        #         # back
        #         nums[start], nums[i] = nums[i], nums[start]
        
        # backtrack(0)
        # return result
