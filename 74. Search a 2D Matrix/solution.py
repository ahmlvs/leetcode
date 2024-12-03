# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        # m = len(matrix)
        # n = len(matrix[0])

        # # first find row
        # left = 0
        # right = m - 1

        # while left < right:
        #     mid = (left + right) // 2

        #     if matrix[mid][n-1] == target:
        #         return True
        #     elif matrix[mid][n-1] > target:
        #         right = mid
        #     else:
        #         left = mid + 1
        
        # # left is correct row
        # # find el in row
        # start = 0
        # end = n - 1

        # while start <= end:
        #     mid = (start + end) // 2

        #     if matrix[left][mid] == target:
        #         return True
        #     elif matrix[left][mid] > target:
        #         end = mid - 1
        #     else:
        #         start = mid + 1
        
        # return False

        # in one step
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            # map mid to correct ind
            mid_value = matrix[mid // n][mid % n]
            if mid_value == target:
                return True
            elif mid_value > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
