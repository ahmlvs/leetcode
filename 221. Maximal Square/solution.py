# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.


from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_side = int(matrix[0][0])

        # dp to hold max square right down corner
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = int(matrix[0][0])

        # first row
        for j in range(1, n):
            dp[0][j] = int(matrix[0][j])
            max_side = max(max_side, dp[0][j])
        
        # first col
        for i in range(1, m):
            dp[i][0] = int(matrix[i][0])
            max_side = max(max_side, dp[i][0])
        
        # rest dp. idea for right down corner
        # 1,2
        # 3,x
        # x = min(1,2,3) + 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0
                max_side = max(max_side, dp[i][j])
        
        return max_side * max_side
