class Node(object):
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class DoubleLinkList(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def addFirst(self, node):
        self.size += 1
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def removeLast(self):
        temp = self.tail.pre
        self.remove(temp)
        return temp

    def remove(self, node):
        self.size -= 1
        node.pre.next = node.next
        node.next.pre = node.pre

    def size(self):
        return self.size


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hashDict = {}
        self.dlink = DoubleLinkList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hashDict:
            return -1
        val = self.hashDict[key].val
        self.put(key, val)
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = Node(key, value)
        if key in self.hashDict:
            self.dlink.remove(self.hashDict[key])
            self.dlink.addFirst(node)
            self.hashDict[key] = node
        else:
            if self.dlink.size == self.capacity:
                last = self.dlink.removeLast()
                del self.hashDict[last.key]
            self.dlink.addFirst(node)
            self.hashDict[key] = node
        return


if __name__ == "__main__":
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    print obj.get(1)
    obj.put(3, 3)
    print obj.get(2)
    obj.put(4, 4)
    print obj.get(1)
    print obj.get(3)
    print obj.get(4)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)