# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

# You start on square 1 of the board. In each move, starting from square curr, do the following:

# Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
# This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
# If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
# The game ends when you reach the square n2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

# Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

# For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.

 

# Example 1:


# Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation: 
# In the beginning, you start at square 1 (at row 5, column 0).
# You decide to move to square 2 and must take the ladder to square 15.
# You then decide to move to square 17 and must take the snake to square 13.
# You then decide to move to square 14 and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# This is the lowest possible number of moves to reach the last square, so return 4.
# Example 2:

# Input: board = [[-1,-1],[-1,3]]
# Output: 1
 

# Constraints:

# n == board.length == board[i].length
# 2 <= n <= 20
# board[i][j] is either -1 or in the range [1, n2].
# The squares labeled 1 and n2 are not the starting points of any snake or ladder.

from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # idea transfor 2d to 1d
        def get_1d_position(square):
            # we work with indexes
            # so square - 1
            row = (square - 1) // n
            col = (square - 1) % n
            if row % 2 == 0:
                # normal direction
                return n - 1 - row, col
            else:
                # reversal direction
                return n - 1 - row, n - 1 - col
        
        board_1d = [-1] * (n * n)
        # board_1d[0] = -1 
        # Squares 1 and n2 are not 
        #the starting points of any snake or ladder.
        for square in range(1, n * n + 1):
            r, c = get_1d_position(square)
            # indexes
            board_1d[square - 1] = board[r][c]
        
        # build queue to save (square, rolls)
        queue = deque([(1, 0)])
        # set to mark visited
        visited = set()

        # let's add all posible variant to queue
        # the shortest path will be in queue earlier
        while queue:
            curr, rolls = queue.popleft()

            # check is it last square
            if curr == n * n:
                return rolls

            # add all possibel vars
            for next_square in range(curr + 1, min(curr + 6, n * n) + 1):
                # check if already visited 
                if next_square in visited:
                    continue
                
                visited.add(next_square)

                if board_1d[next_square - 1] != -1:
                    # snake or ledder
                    queue.append((board_1d[next_square - 1], rolls + 1))
                else:
                    # just next_square
                    queue.append((next_square, rolls + 1))
        
        # if we not found path to last squere with BFS
        return -1
