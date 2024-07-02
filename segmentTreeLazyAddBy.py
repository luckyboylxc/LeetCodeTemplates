class SegTreeMax:
    #update by range adding, query range max
    def __init__(self, data):
        self.data = data
        self.tree = [float('-inf')] * (4 * len(self.data))
        self.lazy = [0] * (4 * len(self.data))
        self.build(1, 0, len(self.data) - 1)

    def build(self, i, tl, tr):
        if tl == tr:
            self.tree[i] = self.data[tl]
            return
        m = tl + (tr-tl)//2
        self.build(i * 2, tl, m)
        self.build(i * 2 + 1, m + 1, tr )
        self.tree[i] =  max(self.tree[2*i], self.tree[2*i+1])
        
    def _update(self, i, ql, qr, add, tl, tr):
        if qr < tl or tr < ql:  # [ql, qr] and [tl, tr] don't intersect.
            return
        
        # 当前区间为修改区间的子集时直接修改当前节点的值, 然后打标记, 结束修改
        if ql <= tl and tr <= qr:  # [ql, qr] includes [tl, tr].
            self.tree[i] = self.tree[i] + add
            self.lazy[i] += add
            return
        
        m = tl + (tr-tl)//2

        if(self.lazy[i]):
            # 如果当前节点的懒标记非空, 则更新当前节点两个子节点的值和懒标记值
            self.tree[i*2] = self.tree[i*2] + self.lazy[i]
            self.tree[i*2 + 1] = self.tree[i*2 + 1] + self.lazy[i]
            # 将标记下传给子节点
            self.lazy[2*i] += self.lazy[i]
            self.lazy[2*i+1] += self.lazy[i]
            # 清空当前节点的标记            
            self.lazy[i] = 0

        if(ql<=m):
            self._update(i * 2, ql, qr, add, tl, m)
        if(qr>m):
            self._update(i * 2 + 1, ql, qr, add, m + 1, tr)
        
        self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])


    def _query(self, i, ql, qr, tl, tr):
        if qr < tl or tr < ql:
            return 0
        # 当前区间为询问区间的子集时直接返回当前区间的和
        if ql <= tl and tr <= qr:  # [ql, qr] includes [tl, tr].
            return self.tree[i]
        
        m = tl + (tr-tl)//2
        if(self.lazy[i]):
            # 如果当前节点的懒标记非空, 则更新当前节点两个子节点的值和懒标记值
            self.tree[i*2] = self.tree[i*2] + self.lazy[i]
            self.tree[i*2 + 1] = self.tree[i*2 + 1] + self.lazy[i]
            # 将标记下传给子节点
            self.lazy[2*i] += self.lazy[i]
            self.lazy[2*i+1] += self.lazy[i]
            # 清空当前节点的标记            
            self.lazy[i] = 0

        sum = float('-inf')
        if(ql<=m):
            sum = max(sum,self._query(i * 2, ql, qr, tl, m))
        if(qr>m):
            sum = max(sum,self._query(i * 2 + 1, ql, qr, m + 1, tr))
        
        return sum
        

    def update(self, left, right, add):
        self._update(1, left+1, right+1, add, 1, len(self.data))

    def query(self, left, right):
        return self._query(1, left+1, right+1, 1, len(self.data))
    
class SegTreeAddBy:
    def __init__(self, data):
        self.data = data
        self.tree = [0] * (4 * len(self.data))
        self.lazy = [0] * (4 * len(self.data))
        self.build(1, 0, len(self.data) - 1)

    def build(self, i, tl, tr):
        if tl == tr:
            self.tree[i] = self.data[tl]
            return
        m = tl + (tr-tl)//2
        self.build(i * 2, tl, m)
        self.build(i * 2 + 1, m + 1, tr )
        self.tree[i] =  self.tree[2*i] + self.tree[2*i+1]
        
    def _update(self, i, ql, qr, add, tl, tr):
        if qr < tl or tr < ql:  # [ql, qr] and [tl, tr] don't intersect.
            return
        
        # 当前区间为修改区间的子集时直接修改当前节点的值, 然后打标记, 结束修改
        if ql <= tl and tr <= qr:  # [ql, qr] includes [tl, tr].
            self.tree[i] = self.tree[i] + (tr-tl + 1)*add
            self.lazy[i] += add
            return
        
        m = tl + (tr-tl)//2

        if(self.lazy[i]):
            # 如果当前节点的懒标记非空, 则更新当前节点两个子节点的值和懒标记值
            self.tree[i*2] = self.tree[i*2] + (m-tl + 1) * self.lazy[i]
            self.tree[i*2 + 1] = self.tree[i*2 + 1] + (tr-m) * self.lazy[i]
            # 将标记下传给子节点
            self.lazy[2*i] += self.lazy[i]
            self.lazy[2*i+1] += self.lazy[i]
            # 清空当前节点的标记            
            self.lazy[i] = 0

        if(ql<=m):
            self._update(i * 2, ql, qr, add, tl, m)
        if(qr>m):
            self._update(i * 2 + 1, ql, qr, add, m + 1, tr)
        
        self.tree[i] = self.tree[2*i] + self.tree[2*i+1]


    def _query(self, i, ql, qr, tl, tr):
        if qr < tl or tr < ql:
            return 0
        # 当前区间为询问区间的子集时直接返回当前区间的和
        if ql <= tl and tr <= qr:  # [ql, qr] includes [tl, tr].
            return self.tree[i]
        
        m = tl + (tr-tl)//2
        if(self.lazy[i]):
            # 如果当前节点的懒标记非空, 则更新当前节点两个子节点的值和懒标记值
            self.tree[i*2] = self.tree[i*2] + (m-tl + 1) * self.lazy[i]
            self.tree[i*2 + 1] = self.tree[i*2 + 1] + (tr-m) * self.lazy[i]
            # 将标记下传给子节点
            self.lazy[2*i] += self.lazy[i]
            self.lazy[2*i+1] += self.lazy[i]
            # 清空当前节点的标记            
            self.lazy[i] = 0
        sum = 0
        if(ql<=m):
            sum += self._query(i * 2, ql, qr, tl, m)
        if(qr>m):
            sum += self._query(i * 2 + 1, ql, qr, m + 1, tr)
        
        return sum
        

    def update(self, left, right, add):
        self._update(1, left+1, right+1, add, 1, len(self.data))

    def query(self, left, right):
        return self._query(1, left+1, right+1, 1, len(self.data))