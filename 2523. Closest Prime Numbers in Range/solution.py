# Given two positive integers left and right, find the two integers num1 and num2 such that:

# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

# Example 1:

# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
# Since 11 is smaller than 17, we return the first pair.
# Example 2:

# Input: left = 4, right = 6
# Output: [-1,-1]
# Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

# Constraints:

# 1 <= left <= right <= 106

from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right + 1)
        is_prime[0], is_prime[1] = False, False
        
        for num in range(2, int((right+1)**0.5)+1):
            if is_prime[num]:
                for m in range(num*num, right+1, num):
                    is_prime[m] = False

        primes = [num for num in range(left, right+1) if is_prime[num]]
        
        if len(primes) < 2:
            return [-1, -1]
        
        min_diff = float('inf')
        ans = [-1, -1]
        
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < min_diff:
                min_diff = primes[i + 1] - primes[i]
                ans = [primes[i], primes[i + 1]]
        
        return ans
