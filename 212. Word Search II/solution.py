# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

# Example 1:


# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:


# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.


from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # let's build trie from words
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            # mark word end
            node.word = word
        
        rows, cols = len(board), len(board[0])
        result = []
        # up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backtrack(row, col, parent):
            char = board[row][col]
            currNode = parent.children[char]

            # check if we found word
            if currNode.word:
                result.append(currNode.word)
                # delete in from Trie
                # because of duplicates
                currNode.word = None
            
            # mark cell as temp visited
            board[row][col] = "#"

            # start all directions
            for dx, dy in directions:
                newRow, newCol = row + dx, col + dy
                if 0 <= newRow < rows and 0 <= newCol < cols and board[newRow][newCol] in currNode.children:
                    backtrack(newRow, newCol, currNode)

            # mark back cell as char
            board[row][col] = char

            # delete child TrieNode if no more children
            # no need more to track
            if not currNode.children:
                parent.children.pop(char)

        # backtrack from all cells
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in root.children:
                    backtrack(i, j, root)

        return result
