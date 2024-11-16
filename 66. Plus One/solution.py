# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # n = len(digits)
        # # for result
        # result = []

        # # saved is for next digit
        # saved = 1
        # # up for current
        # up = 0

        # for i in range(n-1,-1,-1):
        #     # new digit is actual + saved
        #     d = digits[i] + saved
        #     # update saved and up
        #     saved = d // 10
        #     up = d % 10
        #     result.append(up)
        
        # # if saved > 0 add it to result
        # if saved != 0:
        #     result.append(saved)
        
        # # reverse result
        # return result[::-1]

        ## another idea
        ## we add 1. so if last digit < 9 nothing changes
        ## if it is 9, we have moved 1 for next digits
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            # if new < 10 nothing changes
            if digits[i] < 10:
                return digits
            # if > 10 this digit 0
            # and next + 1
            digits[i] = 0
        
        # if all digits were 9, we'll have a carry-over
        return [1] + digits
