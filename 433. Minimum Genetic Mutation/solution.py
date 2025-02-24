# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

# Example 1:

# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
# Example 2:

# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
 

# Constraints:

# 0 <= bank.length <= 10
# startGene.length == endGene.length == bank[i].length == 8
# startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # func to check if only 1 mutation diff
        def is_one_mutation(s1, s2):
            return sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1
        
        bank_set = set(bank)
        
        # check if endGene in bank_set
        # if not we can't reach endGene
        if endGene not in bank_set:
            return -1
        
        # queue (gene, mutations) and visited
        queue = deque([(startGene, 0)])
        visited = set([startGene])

        while queue:
            current_gene, mutations = queue.popleft()

            # check if gene is endGene
            if current_gene == endGene:
                return mutations
            
            # select one by one genes from bank
            for gene in bank:
                if gene not in visited and is_one_mutation(gene, current_gene):
                    visited.add(gene)
                    queue.append((gene, mutations + 1))
        
        # if not found
        return -1
