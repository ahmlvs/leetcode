# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 

# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # to check visited cities
        visited = [False] * n
        provinces = 0

        def dfs(city):
            # check all neighbors for city
            for neighbor in range(n):
                # check that city connected to neighbor
                # and not visited
                if isConnected[city][neighbor] and not visited[neighbor]:
                    # mark as visited
                    visited[neighbor] = True
                    # start dfs for this neighbor
                    dfs(neighbor)
        
        # loop for cities
        for i in range(n):
            # check if already visited
            if not visited[i]:
                # mark as visited
                visited[i] = True
                # start dfs for this city
                dfs(i)
                # after dfs we marked all connected cities
                # so add 1 to provinces
                provinces += 1
        
        return provinces
