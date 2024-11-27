# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # # sort by interval end
        # sorted_intervals = sorted(intervals, key=lambda x: x[1])

        # prev_el0, prev_el1 = sorted_intervals[0]
        # result = []

        # for i in range(1, len(intervals)):
        #     el0, el1 = sorted_intervals[i]

        #     if el0 <= prev_el1:
        #         # overlapping
        #         prev_el1 = el1
        #         if el0 < prev_el0:
        #             prev_el0 = el0
        #     else:
        #         # non-overlapping
        #         # add to result
        #         result.append([prev_el0, prev_el1])
        #         prev_el0 = el0
        #         prev_el1 = el1
        
        # # add last el
        # result.append([prev_el0, prev_el1])

        # return result

        # sort by interval start
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        prev_el0, prev_el1 = sorted_intervals[0]
        result = []

        for i in range(1, len(intervals)):
            el0, el1 = sorted_intervals[i]

            if el0 <= prev_el1:
                # overlapping
                if el1 > prev_el1:
                    prev_el1 = el1
            else:
                # non-overlapping
                # add to result
                result.append([prev_el0, prev_el1])
                prev_el0 = el0
                prev_el1 = el1
        
        # add last el
        result.append([prev_el0, prev_el1])

        return result
