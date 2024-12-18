# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
 

# Follow up: Could you use search pruning to make your solution faster with a larger board?


from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        word_lenght = len(word)

        # visited i,j board
        visited = [[False] * n for _ in range(m)]

        def backtrack(r, c, index):
            # finish
            if index == word_lenght:
                return True
            
            # check corners and correct letter and already visited
            if (r < 0 or r > m-1 or \
                c < 0 or c > n-1 or \
                visited[r][c] or \
                board[r][c] != word[index]):
                return False
            
            # temp mark r,c visited
            visited[r][c] = True

            # backtrack in 4 directions
            # need to find 1 route
            if (backtrack(r-1, c, index+1) or \
                backtrack(r, c+1, index+1) or \
                backtrack(r+1, c, index+1) or \
                backtrack(r, c-1, index+1)):
                return True
            
            # back r,c to not visited
            visited[r][c] = False
            # this backtrack level is False
            return False

        for i in range(m):
            for j in range(n):
                # for each i,j we try find first letter (ind 0)
                if backtrack(i, j, 0):
                    # if backtrack True we find all letters
                    return True

        return False
