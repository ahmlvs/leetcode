# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # result = []

        # n = len(intervals)
        # if n == 0:
        #     result.append(newInterval)
        #     return result
        
        # # add newInterval in intervals
        # intervals.append(newInterval)

        # # sort by interval start
        # sorted_intervals = sorted(intervals, key=lambda x: x[0])
        
        # # second. merge intervals
        # prev_el0, prev_el1 = sorted_intervals[0]

        # for i in range(1, len(intervals)):
        #     el0, el1 = sorted_intervals[i]

        #     if el0 <= prev_el1:
        #         # overlapping
        #         if el1 > prev_el1:
        #             prev_el1 = el1
        #     else:
        #         # non-overlapping
        #         # add to result
        #         result.append([prev_el0, prev_el1])
        #         prev_el0 = el0
        #         prev_el1 = el1
        
        # # add last el
        # result.append([prev_el0, prev_el1])

        # return result

        result = []
        i = 0
        n = len(intervals)

        # add to result all intervals before new
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # merge overalpping and add it
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # add tail of intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
