# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # rows
        m = len(grid)
        # columns
        n = len(grid[0])

        # possible directions
        # down, right, up, left
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # queue to hold (row, col, minutes) rotten oranges
        queue = deque()
        # number of initaially fresh oranges
        fresh = 0
        # minutes from start
        minutes = 0

        # create queue and count fresh oranges
        for r in range(m):
            for c in range(n):
                # if 2 -- rotten
                if grid[r][c] == 2:
                    # add to queue with minutes=0
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    # it is fresh
                    fresh += 1

        while queue:
            row, col, minutes = queue.popleft()

            # for each direction from rotten find fresh
            for dr, dc in directions:
                # new row, col
                new_row, new_col = row + dr, col + dc
                # firstly check that new row col valid
                if (0 <= new_row < m) and (0 <= new_col < n) and grid[new_row][new_col] == 1:
                    # change fresh to rotten
                    grid[new_row][new_col] = 2
                    # update fresh count
                    fresh -= 1
                    # add new point to queue
                    queue.append((new_row, new_col, minutes + 1))

        # if no fresh return minutes
        # if fresh actually 0 -> -1
        return minutes if fresh == 0 else -1
