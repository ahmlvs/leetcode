# You are given an array of positive integers nums.

# An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

# prod(arr) is the product of all elements of arr.
# gcd(arr) is the GCD of all elements of arr.
# lcm(arr) is the LCM of all elements of arr.
# Return the length of the longest product equivalent subarray of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.

# The term gcd(a, b) denotes the greatest common divisor of a and b.

# The term lcm(a, b) denotes the least common multiple of a and b.

 

# Example 1:

# Input: nums = [1,2,1,2,1,1,1]

# Output: 5

# Explanation: 

# The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

# Example 2:

# Input: nums = [2,3,4,5,6]

# Output: 3

# Explanation: 

# The longest product equivalent subarray is [3, 4, 5].

# Example 3:

# Input: nums = [1,2,3,1,4,5,1]

# Output: 5

 

# Constraints:

# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10

from typing import List

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxlength = 0

        for start in range(n):
            curr_prod = 1
            curr_gcd = 0
            curr_lcm = 1
            for end in range(start, n):
                curr_prod *= nums[end]
                
                if end == start:
                    curr_gcd = nums[end]
                else:
                    curr_gcd = gcd(curr_gcd, nums[end])
                
                if end == start:
                    curr_lcm = nums[end]
                else:
                    curr_lcm = lcm(curr_lcm, nums[end])

                if curr_prod == curr_gcd * curr_lcm:
                    maxlength = max(maxlength, end - start + 1)

        return maxlength