# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        # pointers for words
        i, j = len(a)-1, len(b)-1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            # get digit or 0
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            total = bit_a + bit_b + carry

            # in result goes only %2
            result.append(str(total % 2))
            carry = total // 2

            # move pointers
            i -= 1
            j -= 1
        
        # result in reversed order
        return "".join(result[::-1])
