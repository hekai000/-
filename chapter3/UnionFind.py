class UF(object):

    def __init__(self, n):
        self.count = n
        self.parent = [0 for _ in range(n)]
        self.size = [0 for _ in range(n)]
        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, p, q):
        rootP = self.parent[p]
        rootQ = self.parent[q]
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.count -= 1
        return
    def countU(self):
        return self.count

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ


if __name__ == "__main__":
    u = UF(9)
    u.union(1, 3)
    u.union(2, 6)
    print u.countU()
    print u.connected(1, 2)
    print u.connected(1, 3)
    u.union(1, 2)
    print u.connected(1, 2)
    print u.connected(1, 3)
    print u.connected(1, 4)
    print u.countU