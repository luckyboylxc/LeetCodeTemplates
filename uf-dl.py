class UF(object):
    def __init__(self, n):
        self.id = list(range(n))
        self.sz = [1] * n

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]]  # path compression
            p = self.id[p]
        return p

    def getSize(self,p):
        pId = self.find(p)
        return self.sz[pId]
    
    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        if self.sz[pId] < self.sz[qId]:
            self.id[pId] = qId
            self.sz[qId] += self.sz[pId]
        else:
            self.id[qId] = pId
            self.sz[pId] += self.sz[qId]
        self.count -= 1


if __name__ == '__main__':
    import sys

    n = int(sys.stdin.readline())
    uf = UF(n)
    for line in sys.stdin:
        p, q = [int(i) for i in line.split()]
        if (uf.connected(p, q)):
            continue
        else:
            uf.union(p, q)
            print("%s %s" % (p, q))
    print(uf.count, "components")
