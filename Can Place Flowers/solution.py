# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        lenght = len(flowerbed)
        can_be_planted = 0

        for i in range(lenght):
            if flowerbed[i] == 0:
                # check prev empty and no out flowerbed
                prev_empty = (i == 0) or (flowerbed[i-1] == 0)
                next_empty = (i == lenght - 1) or (flowerbed[i+1] == 0)

                if prev_empty and next_empty:
                    can_be_planted += 1
                    # set flower in position
                    flowerbed[i] = 1
                
                # actually done
                if can_be_planted >= n:
                    return True
                
        return can_be_planted >= n
