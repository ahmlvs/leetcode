# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

# Example 1:


# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 9


class Solution:
    def totalNQueens(self, n: int) -> int:
        # backtrack with cols with queens and 
        # attacked main diagonals and
        # attacked anti-diagonals
        def backtrack(row, cols, diagonals1, diagonals2):
            # check if we placed all queens
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                diag1 = row + col
                diag2 = row - col

                # check attacked
                if col in cols or diag1 in diagonals1 or diag2 in diagonals2:
                    continue
                
                # if not. place queen, mark cells and backtrack
                cols.add(col)
                diagonals1.add(diag1)
                diagonals2.add(diag2)

                count += backtrack(row + 1, cols, diagonals1, diagonals2)

                # remove queen and unmark cells
                cols.remove(col)
                diagonals1.remove(diag1)
                diagonals2.remove(diag2)

            return count

        return backtrack(0, set(), set(), set())
