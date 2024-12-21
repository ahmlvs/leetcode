# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph dict with []
        # where keys are prereq
        # and in_degree list for each course
        # how many courses needed before this
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # build queue only with 0 in_degree
        # so we can apply to course now
        # queue = deque()
        # for course_n in in_degree:
        #     if course_n == 0:
        #         queue.append(course_n)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        result = []
        
        while queue:
            current = queue.popleft()
            result.append(current)

            # so now we can get courses
            # graph[current]
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                # if it is 0 -- add to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # need to check if all courses in result
        # if not we have cycles and can't pass all courses
        if len(result) == numCourses:
            return result
        else:
            return []
