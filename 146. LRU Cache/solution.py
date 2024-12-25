# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.


class ListNode:
    
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # hashmap to link keys with nodes
        self.cache = {}
        # dummy nodes for head and tail
        # struct: head, node1,node2, ..., tail
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # helper func to remove node from list
    def _remove(self, node: ListNode):
        prev_node = node.prev
        next_node = node.next
        # re-link
        prev_node.next = next_node
        next_node.prev = prev_node
    
    # helper func to add node right after self.head
    def _add_to_head(self, node):
        next_node = self.head.next
        # re-link
        node.prev = self.head
        node.next = next_node
        self.head.next = node
        next_node.prev = node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # move node to head
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update value and move to head
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # create node
            node = ListNode(key, value)
            self.cache[key] = node
            # insert node to head
            self._add_to_head(node)
            # check capacity
            # if more - delete lru
            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
