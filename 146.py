class Node:
    def __init__(self, key = None, val = None):
        self.key, self.val = key, val
        self.left = self.right = None

class LRUCache:
    def __init__(self, capacity: int):
        self.lookup = {}
        self.head, self.tail = Node(), Node()
        self.head.right = self.tail
        self.tail.left = self.head
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        node = self.lookup[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            node.val = value
            self.moveToHead(node)
        else:
            self.lookup[key]= Node(key, value)
            self.addToHead(self.lookup[key])
            if len(self.lookup) > self.cap:
                self.removeTail()
    
    def removeNode(self, node):
        node.left.right = node.right
        node.right.left = node.left
    
    def addToHead(self, node):
        node.left, node.right = self.head, self.head.right
        self.head.right.left = node
        self.head.right = node
    
    def removeTail(self):
        node = self.tail.left
        self.removeNode(node)
        del self.lookup[node.key]
        del node
    
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
