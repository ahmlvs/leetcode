# There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.

# You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.

# Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.

# Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.

# Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

 

# Example 1:

# Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2

# Output: [9,7,9,8,8]

# Explanation:

# For i = 0, connect node 0 from the first tree to node 0 from the second tree.
# For i = 1, connect node 1 from the first tree to node 0 from the second tree.
# For i = 2, connect node 2 from the first tree to node 4 from the second tree.
# For i = 3, connect node 3 from the first tree to node 4 from the second tree.
# For i = 4, connect node 4 from the first tree to node 4 from the second tree.

# Example 2:

# Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1

# Output: [6,3,3,3,3]

# Explanation:

# For every i, connect node i of the first tree with any node of the second tree.


 

# Constraints:

# 2 <= n, m <= 1000
# edges1.length == n - 1
# edges2.length == m - 1
# edges1[i].length == edges2[i].length == 2
# edges1[i] = [ai, bi]
# 0 <= ai, bi < n
# edges2[i] = [ui, vi]
# 0 <= ui, vi < m
# The input is generated such that edges1 and edges2 represent valid trees.
# 0 <= k <= 1000

from collections import deque
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        cnt1 = [0] * n
        m = len(edges2) + 1
        cnt2 = [0] * m

        # bfs for tree1 in k-depth
        graph1 = [[] for _ in range(n)]
        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u in range(n):
            visited = [False] * n
            queue = deque()
            queue.append((u, 0))
            visited[u] = True
            count = 0
            while queue:
                node, dist = queue.popleft()
                if dist > k:
                    break
                count += 1
                # add node neighbors
                for neighbor in graph1[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, dist + 1))
            cnt1[u] = count 

        # bfs for tree2 in (k-1)-depth
        graph2 = [[] for _ in range(m)]
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        for v in range(m):
            visited = [False] * m
            queue = deque()
            queue.append((v, 0))
            visited[v] = True
            count = 0
            while queue:
                node, dist = queue.popleft()
                if dist > k - 1:
                    break
                count += 1
                # add node neighbors
                for neighbor in graph2[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, dist + 1))
            cnt2[v] = count 

        max_cnt2 = max(cnt2)

        answer = [cnt1[u] + max_cnt2 for u in range(n)]
        return answer
