# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

 

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation:


# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

# Example 2:

# Input: board = [["X"]]

# Output: [["X"]]

 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        # idea to find "O" in edges
        # and with dfs find all connected
        # and mark them "S"
        # another "O" change to "X"

        # help dfs func to check all neighbors
        # and mark visited as "S"
        def dfs(r, c):
            # check corners
            # and land or water
            if (r < 0 or r >= m or \
                c < 0 or c >= n or \
                board[r][c] == "X" or \
                board[r][c] == "S"):
                # do nothing
                return
            
            # if ok, mark as visited
            # and start check all neighbors
            board[r][c] = "S"
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r+1, c)
            dfs(r, c-1)
        
        # check edges
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m - 1][j] == "O":
                dfs(m - 1, j)

        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n - 1] == "O":
                dfs(i, n - 1)
        
        # change "S" to "O"
        # and "O" to "X"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"

                if board[i][j] == "S":
                    board[i][j] = "O"
