# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.

from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        # if end not in list - no solution
        if endWord not in wordSet:
            return 0

        # (current_word, steps)
        # beginWord already 1 step
        queue = deque([(beginWord, 1)])

        while queue:
            curr, steps = queue.popleft()

            # try change each letter in word
            for i in range(len(curr)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    # check that char change word
                    if char != curr[i]:
                        new = curr[:i] + char + curr[i+1:]

                        if new == endWord:
                            return steps + 1
                        
                        if new in wordSet:
                            # mark new like visited visited
                            wordSet.remove(new)

                            queue.append((new, steps + 1))
        
        # no transformation path exist
        return 0
