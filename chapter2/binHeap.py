class BinHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def exchange(self, i, j):
        self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]
        return

    def left(self, root):
        return 2*root

    def right(self, root):
        return 2*root + 1

    def parent(self, child):
        return child/2

    def swim(self, n):
        while n > 1 and self.heapList[n] > self.heapList[self.parent(n)]:
            self.exchange(n, self.parent(n))
            n = self.parent(n)
        return

    def sink(self, m):
        while self.left(m) <= self.currentSize:
            older =self.left(m)
            if self.right(m) <= self.currentSize and self.heapList[self.right(m)] > self.heapList[self.left(m)]:
                older = self.right(m)
            if self.heapList[m] >= self.heapList[older]:
                break
            self.exchange(m, older)
            m = older

        return

    def insert(self, e):
        self.currentSize += 1
        self.heapList.append(e)
        self.swim(self.currentSize)
        return

    def delMax(self):
        max_e = self.heapList[1]
        self.exchange(1, self.currentSize)
        self.currentSize -= 1
        self.sink(1)
        return max_e

if __name__ == "__main__":
    q = BinHeap()
    q.insert(1)
    q.insert(2)
    q.insert(3)
    q.insert(9)
    q.insert(5)
    q.delMax()
    q.insert(10)