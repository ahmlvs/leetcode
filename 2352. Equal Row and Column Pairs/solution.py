# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

# Example 1:


# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:


# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]
 

# Constraints:

# n == grid.length == grid[i].length
# 1 <= n <= 200
# 1 <= grid[i][j] <= 105

from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # vocabulary to save rows like tuples
        row_count = {}

        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in row_count:
                row_count[row_tuple] += 1
            else:
                row_count[row_tuple] = 1
        
        number_of_pairs = 0

        # create col tuples and check how many rows are similar
        for c in range(n):
            col_tuple = tuple(grid[r][c] for r in range(n))
            if col_tuple in row_count:
                number_of_pairs += row_count[col_tuple]
        
        return number_of_pairs
