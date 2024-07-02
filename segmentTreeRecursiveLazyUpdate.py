class SegmentTree(object):
    def __init__(self,arr):
        n = len(arr)
        self.size = n 
        total = 2<<(n.bit_length())
        self.tree = [0 for i in range(total)]
        self.lazy = [0 for i in range(total)] 
        #lazy[x] != 0, means that there are updates need to be done on x's child node (left and right child, does not include x)
        
        #self.build(arr,1,0,n-1)

    def build(self,arr,node,l,r):
        # [l,r] represents the interval (in arr) represented by the node in tree t.
        if(l==r):
            self.tree[node] = arr[l]
            return
        
        m = l+(r-l)//2
        self.build(arr,2*node,l,m)
        self.build(arr,2*node+1,m+1,r)
        self.tree[node] = max(self.tree[node],self.tree[2*node], self.tree[2*node + 1])

    def _update(self,node,tl,tr,ql,qr,val):
        
        if(tl>qr or tr<ql):
            return 
        
        if(ql<=tl and tr<=qr):
            self.tree[node] = max(self.tree[node],val)
            self.lazy[node] = max(self.lazy[node],val)
            return
        
        m = tl + (tr-tl)//2
        if(self.lazy[node] !=0):
            # 如果当前节点的懒标记非空, 则更新当前节点两个子节点的值和懒标记值
            self.tree[node*2] = max(self.tree[node*2],self.lazy[node])
            self.tree[node*2+1] = max(self.tree[node*2+1],self.lazy[node])

            self.lazy[node*2] = max(self.lazy[node*2],self.lazy[node])
            self.lazy[node*2+1] = max(self.lazy[node*2+1],self.lazy[node])

            self.lazy[node] = 0

        if(m>=ql):
            self._update(node*2,tl,m,ql,qr,val)
        
        if(m+1<=qr):
            self._update(node*2+1,m+1,tr,ql,qr,val)
        
        self.tree[node] = max(self.tree[node],self.tree[2*node], self.tree[2*node + 1])

    def update(self,ql,qr,val):
        self._update(1,0,self.size-1,ql,qr,val)

    def _query(self,node,tl,tr,ql,qr):
        # [tl,tr] represents the interval (in arr) represented by the node in tree t.
        # [ql,qr] represents the query interval

        #Interval represented by node is completely outside the given interval of [ql,qr]
        if(tl>qr or tr<ql):
            return 0
        
        #Interval represented by node is completely inside the given interval of [ql,qr]
        if(ql<=tl and tr<=qr):
            return self.tree[node]
        
        #Interval represented by node is partially inside and partially outside the given interval of [ql,qr]
        m = tl + (tr-tl)//2
        if(self.lazy[node] !=0):
            # 如果当前节点的懒标记非空, 则更新当前节点两个子节点的值和懒标记值
            self.tree[node*2] = max(self.tree[node*2],self.lazy[node])
            self.tree[node*2+1] = max(self.tree[node*2+1],self.lazy[node])

            self.lazy[node*2] = max(self.lazy[node*2],self.lazy[node])
            self.lazy[node*2+1] = max(self.lazy[node*2+1],self.lazy[node])

            self.lazy[node] = 0

        ans = 0
        if(m>=ql):
            res = self._query(node*2,tl,m,ql,qr)
            ans = max(ans,res)
        if(m+1 <=qr):
            res = self._query(node*2+1,m+1,tr,ql,qr)
            ans = max(ans,res)

        return ans
    
    def query(self,ql,qr):
        return self._query(1,0,self.size-1,ql,qr)