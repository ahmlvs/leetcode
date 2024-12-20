# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph dict
        graph = {i: [] for i in range(numCourses)}

        # {0: [1], 1: []}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # set for visited and on_path nodes
        # if checking each course neighbors
        # we already find it in path
        # it mean we have cycle 
        visited = set()
        on_path = set()
        
        def dfs(course):
            if course in on_path:
                # it is cycle
                return False
            if course in visited:
                # we actullly totally check it
                return True
            
            # add course in on_path 
            # while checking it and neighbors
            on_path.add(course)

            # check all neighbors
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            # mark course as visited
            # and delete from on_path
            visited.add(course)
            on_path.remove(course)

            return True
        
        # check all courses
        for course in range(numCourses):
            if not dfs(course):
                # cicle detected - False
                return False
        
        return True
