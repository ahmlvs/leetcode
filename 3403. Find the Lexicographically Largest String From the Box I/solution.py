# You are given a string word, and an integer numFriends.

# Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

# word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
# All the split words are put into a box.
# Find the lexicographically largest string from the box after all the rounds are finished.

# A string a is lexicographically smaller than a string b if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
# If the first min(a.length, b.length) characters do not differ, then the shorter string is the lexicographically smaller one.

 

# Example 1:

# Input: word = "dbca", numFriends = 2

# Output: "dbc"

# Explanation: 

# All possible splits are:

# "d" and "bca".
# "db" and "ca".
# "dbc" and "a".
# Example 2:

# Input: word = "gggg", numFriends = 4

# Output: "g"

# Explanation: 

# The only possible split is: "g", "g", "g", and "g".

 

# Constraints:

# 1 <= word.length <= 5 * 103
# word consists only of lowercase English letters.
# 1 <= numFriends <= word.length


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # max_string = ""
        
        # def backtrack(start, parts):
        #     nonlocal max_string
            
        #     if len(parts) == numFriends:
        #         if start == len(word):
        #             max_string = max(max_string, max(parts))
        #         return
            
        #     if len(word) - start < numFriends - len(parts):
        #         return
            
        #     for end in range(start + 1, len(word) + 1):
        #         backtrack(end, parts + [word[start:end]])
        
        
        # backtrack(0, [])
        # return max_string
        # LTE

        # n = len(word)
        # dp = [[""] * (numFriends + 1) for _ in range(n + 1)]
        
        # for i in range(1, n + 1):
        #     dp[i][1] = max(dp[i - 1][1], word[:i])
        
        # for k in range(2, numFriends + 1):
        #     for i in range(k, n + 1):
        #         for j in range(k - 1, i):
        #             dp[i][k] = max(dp[i][k], max(dp[j][k - 1], word[j:i]))
        
        # return dp[n][numFriends]
        # LTE

        if numFriends == 1:
            return word
        
        n = len(word)
        max_string = ""
    
        for L in range(n):
            R = min(n - 1, min(L, numFriends - 1) + (n - numFriends))
            candidate = word[L : R + 1]
    
            if candidate > max_string:
                max_string = candidate
    
        return max_string
