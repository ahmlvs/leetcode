# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        if not matrix:
            return result
        
        # corners
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # move from left to right along top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            # increase top
            top += 1

            # move from top to bottom along right col
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            # decrease right
            right -= 1

            # check top and bottom
            if top <= bottom:
                # move from right to left along bottom row
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                # decrease bottom
                bottom -= 1
            
            # check left and right
            if left <= right:
                # move from bottom to top along left col
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                # increase left
                left += 1
        
        return result
