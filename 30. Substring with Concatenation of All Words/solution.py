# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# Explanation:

# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

# Output: []

# Explanation:

# There is no concatenated substring.

# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

# Output: [6,9,12]

# Explanation:

# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

# Constraints:

# 1 <= s.length <= 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.

from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_lenght = len(words[0])
        word_count = len(words)
        words_freq = Counter(words)

        result = []

        # we can start find strings from word_lenght positions
        for i in range(word_lenght):
            # window
            left = i
            right = i
            window_freq = Counter()
            words_used = 0

            while right + word_lenght <= len(s):
                # get word
                word = s[right:right + word_lenght]
                # move right
                right += word_lenght

                if word in words_freq:
                    window_freq[word] += 1
                    words_used += 1

                    # check if window_freq[word] <= words_freq[word]
                    # if not need to move window left side
                    # and delete left word
                    while window_freq[word] > words_freq[word]:
                        left_word = s[left:left + word_lenght]
                        window_freq[left_word] -= 1
                        words_used -= 1
                        left += word_lenght

                    # if we found all words
                    if words_used == word_count:
                        result.append(left)

                else:
                    # move window
                    left = right
                    # reset counter
                    window_freq.clear()
                    words_used = 0
        
        return result
