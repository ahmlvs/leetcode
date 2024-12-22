# You are given an integer array nums and an integer k.

# You are allowed to perform the following operation on each element of the array at most once:

# Add an integer in the range [-k, k] to the element.
# Return the maximum possible number of distinct elements in nums after performing the operations.

 

# Example 1:

# Input: nums = [1,2,2,3,3,4], k = 2

# Output: 6

# Explanation:

# nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

# Example 2:

# Input: nums = [4,4,4,4], k = 1

# Output: 3

# Explanation:

# By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].

 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= k <= 109

from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # num_sorted = sorted(nums)
        # used_values = set()

        # for num in num_sorted:
        #     # print(used_values)
        #     for v in range(num - k, num + k + 1):
        #         if v not in used_values:
        #             used_values.add(v)
        #             break

        # return len(used_values)

        num_sorted = sorted(nums)
        curr_max = float("-inf")
        count = 0

        for num in num_sorted:
            new_v = max(num - k, curr_max + 1)
            if new_v <= num + k:
                curr_max = new_v
                count += 1

        return count
