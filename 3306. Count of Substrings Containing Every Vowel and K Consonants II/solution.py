# You are given a string word and a non-negative integer k.

# Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

# Example 1:

# Input: word = "aeioqq", k = 1

# Output: 0

# Explanation:

# There is no substring with every vowel.

# Example 2:

# Input: word = "aeiou", k = 0

# Output: 1

# Explanation:

# The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

# Example 3:

# Input: word = "ieaouqqieaouqq", k = 1

# Output: 3

# Explanation:

# The substrings with every vowel and one consonant are:

# word[0..5], which is "ieaouq".
# word[6..11], which is "qieaou".
# word[7..12], which is "ieaouq".
 

# Constraints:

# 5 <= word.length <= 2 * 105
# word consists only of lowercase English letters.
# 0 <= k <= word.length - 5

from collections import defaultdict
import bisect

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = set('aeiou')
        
        prefix_consonant = [0] * (n + 1)
        for i in range(n):
            prefix_consonant[i + 1] = prefix_consonant[i] + (1 if word[i] not in vowels else 0)
        
        consonant_dict = defaultdict(list)
        for i in range(n + 1):
            consonant_dict[prefix_consonant[i]].append(i)
        
        count = 0
        last_occurrence = {v: -1 for v in vowels}

        for r in range(n):
            ch = word[r]
            if ch in vowels:
                last_occurrence[ch] = r

            if any(last_occurrence[v] == -1 for v in vowels):
                continue
            
            min_last = min(last_occurrence.values())
            
            target = prefix_consonant[r + 1] - k
            if target < 0:
                continue
            
            valid_count = bisect.bisect_right(consonant_dict[target], min_last)
            count += valid_count
        
        return count
