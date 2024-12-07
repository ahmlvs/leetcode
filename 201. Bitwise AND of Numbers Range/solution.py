# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

# Example 1:

# Input: left = 5, right = 7
# Output: 4
# Example 2:

# Input: left = 0, right = 0
# Output: 0
# Example 3:

# Input: left = 1, right = 2147483647
# Output: 0
 

# Constraints:

# 0 <= left <= right <= 231 - 1


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 101 - 5
        # 110
        # 111 - 7
        # bitwise AND 1 + 1 = 1, 1 + 0 = 0, 0 + 0 = 0
        # so if in one column is 0 - all column 0
        # need to find all columns equal to 1's and shift

        shift = 0

        while left < right:
            # right shift
            left >>= 1
            right >>= 1
            shift += 1
        
        # left shift
        return left << shift
