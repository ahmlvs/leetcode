# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        islands_count = 0

        # help dfs func to check all neighbors
        # and mark visited as "0"
        def dfs(r, c):
            # check corners
            # and land or water
            if (r < 0 or r >= m or \
                c < 0 or c >= n or \
                grid[r][c] == "0"):
                # do nothing
                return
            
            # if ok, mark as visited
            # and start check all neighbors
            grid[r][c] = "0"
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r+1, c)
            dfs(r, c-1)
        

        # check all cells
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # start dfs from this cell
                    dfs(i, j)
                    islands_count += 1
        
        return islands_count
