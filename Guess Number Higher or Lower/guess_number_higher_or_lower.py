# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

 

# Example 1:

# Input: n = 10, pick = 6
# Output: 6
# Example 2:

# Input: n = 1, pick = 1
# Output: 1
# Example 3:

# Input: n = 2, pick = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 231 - 1
# 1 <= pick <= n

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def __init__(self, pick: int):
        self.pick = pick
    
    def guess(self, num: int) -> int:
        if num > self.pick:
            return -1
        elif num < self.pick:
            return 1
        else:
            return 0

    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            num = (low + high) // 2

            # get guess result
            guess_result = self.guess(num)

            if guess_result == 0:
                return num # num = pick
            elif guess_result == 1:
                low =  num + 1 # guess is lower
            else:
                high = num - 1 # guess is higher
        
        return -1 # if cases valid, should never reach here
