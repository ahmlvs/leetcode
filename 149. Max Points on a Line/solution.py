# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

# Example 1:


# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# Example 2:


# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
 

# Constraints:

# 1 <= points.length <= 300
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.


from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def coef(p1, p2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]

            if dx == 0:
                # vertical line
                return ('inf', 0)
            if dy == 0:
                # horizontal line
                return (0, 'inf')
            
            # gcd to small coef
            d = gcd(dx, dy)
            dx //= d
            dy //= d

            # (-1, 2) and (1, -2)
            # to one struct
            if dx < 0:
                dx, dy = -dx, -dy

            return (dx, dy)
        
        n = len(points)
        # edge case
        if n <= 2:
            return n
        
        max_points = 0

        # iterate for each point. and find coef for each pair
        for i in range(n):
            coefs = defaultdict(int)
            duplicates = 0
            for j in range(i+1, n):
                if points[i] == points[j]:
                    # duplicate
                    duplicates += 1
                    continue
                
                c = coef(points[i], points[j])
                coefs[c] += 1

                # update max_points
                # max in coefs
                # duplicate
                # and init point
                max_points = max(max_points, max(coefs.values(), default=0) + duplicates + 1)

        return max_points
