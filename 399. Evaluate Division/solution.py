# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

# Example 1:

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0
# Example 2:

# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:

# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
 

# Constraints:

# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.

from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # create graph for all equations
        # and equations^-1 with values
        # like dict of dicts
        graph = defaultdict(dict)
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value
        
        # dfs func for search
        # node - first arg for query
        # target - second arg for query
        # visited - set to track keys
        # value - actual value

        def dfs(node, target, visited, value):
            # if node == target need to finish
            # we found actual value
            if node == target:
                return value
            
            # start search target for node in graph
            for neighbor, weight in graph[node].items():
                # check if neighbor already visited
                if neighbor not in visited:
                    # mark as visited
                    visited.add(neighbor)
                    # start dfs for this neighbor
                    # with new value = value * weight
                    result = dfs(neighbor, target, visited, value * weight)
                    # if result == -1.0
                    # it means not found target
                    # so continue. if found return it
                    if result != -1.0:
                        return result
            
            # if we a here -- not found target
            return -1.0
        
        # results for each queries
        results = []

        for C, D in queries:
            # if C and D valid keys
            if C in graph and D in graph:
                # if C == D return 1.0
                if C == D:
                    results.append(1.0)
                else:
                    # start dfs search
                    # empty set and start value 1.0
                    results.append(dfs(C, D, set(), 1.0))
            else: # no C or D in graph
                results.append(-1.0)

        return results
