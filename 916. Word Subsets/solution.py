# You are given two string arrays words1 and words2.

# A string b is a subset of string a if every letter in b occurs in a including multiplicity.

# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.

# Return an array of all the universal strings in words1. You may return the answer in any order.

 

# Example 1:

# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
# Output: ["facebook","google","leetcode"]
# Example 2:

# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
# Output: ["apple","google","leetcode"]
 

# Constraints:

# 1 <= words1.length, words2.length <= 104
# 1 <= words1[i].length, words2[i].length <= 10
# words1[i] and words2[i] consist only of lowercase English letters.
# All the strings of words1 are unique.

from collections import Counter, defaultdict
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # max freq for words2
        max_freq = defaultdict(int)

        # add max freq of chars in words2
        for word2 in words2:
            w2_c = Counter(word2)
            for char in w2_c:
                max_freq[char] = max(max_freq[char], w2_c[char])
            # print(w2_c, max_freq)
        
        result = []
        # check words1 
        for word1 in words1:
            w1_c = Counter(word1)
            if all(w1_c[char] >= max_freq[char] for char in max_freq):
                result.append(word1)

        return result
