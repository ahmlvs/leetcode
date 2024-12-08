# You are given an array points where points[i] = [xi, yi] represents the coordinates of a point on an infinite plane.

# Your task is to find the maximum area of a rectangle that:

# Can be formed using four of these points as its corners.
# Does not contain any other point inside or on its border.
# Has its edges parallel to the axes.
# Return the maximum area that you can obtain or -1 if no such rectangle is possible.

 

# Example 1:

# Input: points = [[1,1],[1,3],[3,1],[3,3]]

# Output: 4

# Explanation:

# Example 1 diagram

# We can make a rectangle with these 4 points as corners and there is no other point that lies inside or on the border. Hence, the maximum possible area would be 4.

# Example 2:

# Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]

# Output: -1

# Explanation:

# Example 2 diagram

# There is only one rectangle possible is with points [1,1], [1,3], [3,1] and [3,3] but [2,2] will always lie inside it. Hence, returning -1.

# Example 3:

# Input: points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]

# Output: 2

# Explanation:

# Example 3 diagram

# The maximum area rectangle is formed by the points [1,3], [1,2], [3,2], [3,3], which has an area of 2. Additionally, the points [1,1], [1,2], [3,1], [3,2] also form a valid rectangle with the same area.

 

# Constraints:

# 1 <= points.length <= 10
# points[i].length == 2
# 0 <= xi, yi <= 100
# All the given points are unique.

from typing import List

class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        max_area = -1
        n = len(points)
        points_set = set(map(tuple, points))

        for i in range(n):
            # check all next
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 != x2 and y1 != y2:
                    # check parallel
                    if (x1, y2) in points_set and (x2, y1) in points_set:
                        area = abs(x1-x2) * abs(y1-y2)

                        # check no points
                        no_points = True
                        min_x = min(x1, x2)
                        max_x = max(x1, x2)
                        min_y = min(y1, y2)
                        max_y = max(y1, y2)
                        for x in range(min_x, max_x + 1):
                            for y in range(min_y, max_y + 1):
                                if (x, y) in points_set and (x, y) != (x1, y1) and (x, y) != (x1, y2) and (x, y) != (x2, y1) and (x, y) != (x2, y2):
                                    no_points = False
                                    break
                            # if 1 point in
                            if not no_points:
                                break

                        if no_points:
                            max_area = max(area, max_area)

        return max_area
