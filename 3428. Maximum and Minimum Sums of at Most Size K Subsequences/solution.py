# You are given an integer array nums and a positive integer k. Return the sum of the maximum and minimum elements of all subsequences of nums with at most k elements.

# A non-empty subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [1,2,3], k = 2

# Output: 24

# Explanation:

# The subsequences of nums with at most 2 elements are:

# Subsequence	Minimum	Maximum	Sum
# [1]	1	1	2
# [2]	2	2	4
# [3]	3	3	6
# [1, 2]	1	2	3
# [1, 3]	1	3	4
# [2, 3]	2	3	5
# Final Total	 	 	24
# The output would be 24.

# Example 2:

# Input: nums = [5,0,6], k = 1

# Output: 22

# Explanation:

# For subsequences with exactly 1 element, the minimum and maximum values are the element itself. Therefore, the total is 5 + 5 + 0 + 0 + 6 + 6 = 22.

# Example 3:

# Input: nums = [1,1,1], k = 2

# Output: 12

# Explanation:

# The subsequences [1, 1] and [1] each appear 3 times. For all of them, the minimum and maximum are both 1. Thus, the total is 12.

 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 1 <= k <= min(100, nums.length)

from typing import List


MOD = 10**9 + 7

def factorials(n_max):
    fact = [1]*(n_max+1)
    inv_fact = [1]*(n_max+1)
    for i in range(1, n_max+1):
        fact[i] = fact[i-1]*i % MOD
    
    inv_fact[n_max] = pow(fact[n_max], MOD-2, MOD)
    for i in reversed(range(n_max)):
        inv_fact[i] = (inv_fact[i+1]*(i+1)) % MOD
    
    return fact, inv_fact

def ncr(n, r, fact, inv_fact):
    if r < 0 or r > n:
        return 0
    return fact[n]*inv_fact[r]%MOD * inv_fact[n-r]%MOD

class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        fact, inv_fact = factorials(n)

        pcomb = [0]*n
        pcomb[0] = 1
        
        for i in range(1, n):
            val = 2*pcomb[i-1] % MOD
            if i-1 >= k-1:
                c = ncr(i-1, k-1, fact, inv_fact)
                val = (val - c) % MOD
            pcomb[i] = val

        sum_max_i = 0
        sum_min_i = 0
        for i in range(n):
            sum_max_i = (sum_max_i + nums[i]*pcomb[i]) % MOD
            sum_min_i = (sum_min_i + nums[i]*pcomb[n-1 - i]) % MOD

        return (sum_max_i + sum_min_i) % MOD
