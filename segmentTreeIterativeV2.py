class SegmentTree:
    def __init__(self, data):
        self.data = data
        n = len(data)
        self.tree = [[0 for i in range(4)] for _ in range(2<<n.bit_length()) ]
        self.build(self.tree, 1, 0, n - 1)

    def maintain(self,t,o):
        a,b = t[2*o], t[2*o+1]
        #print(o)
        t[o][0] = max(a[1]+b[0],a[0]+b[2])
        t[o][1] = max(a[1]+b[1],a[0]+b[3])
        t[o][2] = max(a[2]+b[2],a[3]+b[0])
        t[o][3] = max(a[2]+b[3],a[3]+b[1])

    def build(self,t,o, l, r):
        #o: node in segment tree
        #l,r: idx in data 
        if l == r:
            t[o][3] = max(self.data[l],0)
            return
    
        m = l + (r-l)//2

        self.build(t,o * 2, l, m)
        self.build(t,o * 2 + 1, m + 1, r )
        self.maintain(t,o)
        
    def _update(self, t, o, l, r, i,val):
        if(l==r):
            t[o][3] = max(val,0)
            return 

        m = (l+r)//2
        if(i<=m):
            self._update(t,2*o,l,m,i,val)
        else:
            self._update(t,2*o+1,m+1,r,i,val)
        self.maintain(t,o)
    def update(self,i,val):
        self._update(self.tree, 1,0,len(self.data)-1,i,val)
    def query(self,i):
        return self.tree[i][3]