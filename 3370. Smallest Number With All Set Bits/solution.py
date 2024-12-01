# You are given a positive number n.

# Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits.

# A set bit refers to a bit in the binary representation of a number that has a value of 1.

 

# Example 1:

# Input: n = 5

# Output: 7

# Explanation:

# The binary representation of 7 is "111".

# Example 2:

# Input: n = 10

# Output: 15

# Explanation:

# The binary representation of 15 is "1111".

# Example 3:

# Input: n = 3

# Output: 3

# Explanation:

# The binary representation of 3 is "11".

 

# Constraints:

# 1 <= n <= 1000


class Solution:
    def smallestNumber(self, n: int) -> int:
        x = n
        while True:
            if bin(x).count('0') == 1:
                return x
            x += 1
    