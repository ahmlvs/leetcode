# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.

 

# Example 1:

# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
# Example 2:

# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# Explanation: The only word "havana" will be always suggested while typing the search word.
 

# Constraints:

# 1 <= products.length <= 1000
# 1 <= products[i].length <= 3000
# 1 <= sum(products[i].length) <= 2 * 104
# All the strings of products are unique.
# products[i] consists of lowercase English letters.
# 1 <= searchWord.length <= 1000
# searchWord consists of lowercase English letters.

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            # add up to 3 words to suggestions
            if len(node.suggestions) < 3:
                node.suggestions.append(word)
    
    def get_suggestions(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.suggestions

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # ## because 1 <= products.length <= 1000
        # ## we can use brute force
        
        # result = []
        # prefix = ""
        # # sort the products lexicographically
        # sorted_products = sorted(products)

        # for char in searchWord:
        #     prefix += char
        #     find_products = [product for product in sorted_products if product.startswith(prefix)]
        #     result.append(find_products[:3])
        
        # return result

        ## trie approach
        result = []
        prefix = ""
        # sort the products lexicographically
        sorted_products = sorted(products)

        # insert sorted_products in Trie
        trie = Trie()
        for product in sorted_products:
            trie.insert(product)

        # find suggestions
        for char in searchWord:
            prefix += char
            result.append(trie.get_suggestions(prefix))
        
        return result
