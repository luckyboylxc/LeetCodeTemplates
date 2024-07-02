class SegmentTree(object):
    def __init__(self,arr):
        n = len(arr)
        self.size = n 
        total = 2<<(n.bit_length())
        self.tree = [0 for i in range(total)]
        self.build(self.tree,arr,1,0,n-1)

    def build(self,t,arr,node,l,r):
        # [l,r] represents the interval (in arr) represented by the node in tree t.
        if(l==r):
            t[node] = arr[l]
            return
        
        m = l+(r-l)//2
        self.build(t,arr,2*node,l,m)
        self.build(t,arr,2*node+1,m+1,r)
        t[node] = t[2*node] + t[2*node + 1]

    def _update(self,t,node,l,r,idx,val):
        if(l==r):
            t[node] = val
            return
        
        m = l + (r-l)//2
        if(idx<=m):
            self._update(t,node*2,l,m,idx,val)
        else:
            self._update(t,node*2+1,m+1,r,idx,val)
        
        t[node] = t[2*node] + t[2*node + 1]

    def update(self,idx,val):
        self._update(self.tree,1,0,self.size-1,idx,val)

    def _query(self,t,node,tl,tr,ql,qr):
        # [tl,tr] represents the interval (in arr) represented by the node in tree t.
        # [ql,qr] represents the query interval

        #Interval represented by node is completely outside the given interval of [ql,qr]
        if(tl>qr or tr<ql):
            return 0
        
        #Interval represented by node is completely inside the given interval of [ql,qr]
        if(ql<=tl and tr<=qr):
            return t[node]
        
        #Interval represented by node is partially inside and partially outside the given interval of [ql,qr]
        m = tl + (tr-tl)//2
        lt = self._query(t,node*2,tl,m,ql,qr)
        rt = self._query(t,node*2+1,m+1,tr,ql,qr)
        return lt+rt
    
    def queryRangeSum(self,ql,qr):
        return self._query(self.tree,1,0,self.size-1,ql,qr)
    
class SegmentTreeMax(object):
    def __init__(self,arr):
        n = len(arr)
        self.size = n 
        total = 2<<(n.bit_length())
        self.tree = [float('-inf') for i in range(total)]
        self.build(self.tree,arr,1,0,n-1)

    def build(self,t,arr,node,l,r):
        # [l,r] represents the interval (in arr) represented by the node in tree t.
        if(l==r):
            t[node] = arr[l]
            return
        
        m = l+(r-l)//2
        self.build(t,arr,2*node,l,m)
        self.build(t,arr,2*node+1,m+1,r)
        t[node] = max(t[2*node],t[2*node + 1])

    def _update(self,t,node,l,r,idx,val):
        if(l==r):
            t[node] = val
            return
        
        m = l + (r-l)//2
        if(idx<=m):
            self._update(t,node*2,l,m,idx,val)
        else:
            self._update(t,node*2+1,m+1,r,idx,val)
        
        t[node] = max(t[2*node],t[2*node + 1])

    def update(self,idx,val):
        self._update(self.tree,1,0,self.size-1,idx,val)

    def _query(self,t,node,tl,tr,ql,qr):
        # [tl,tr] represents the interval (in arr) represented by the node in tree t.
        # [ql,qr] represents the query interval

        #Interval represented by node is completely outside the given interval of [ql,qr]
        if(tl>qr or tr<ql):
            return float('-inf')
        
        #Interval represented by node is completely inside the given interval of [ql,qr]
        if(ql<=tl and tr<=qr):
            return t[node]
        
        #Interval represented by node is partially inside and partially outside the given interval of [ql,qr]
        m = tl + (tr-tl)//2
        lt = self._query(t,node*2,tl,m,ql,qr)
        rt = self._query(t,node*2+1,m+1,tr,ql,qr)
        return max(lt,rt)
    
    def queryMax(self,ql,qr):
        return self._query(self.tree,1,0,self.size-1,ql,qr)


class SegmentTreeMin(object):
    def __init__(self,arr):
        n = len(arr)
        self.size = n 
        total = 2<<(n.bit_length())
        self.tree = [float('inf') for i in range(total)]
        self.build(self.tree,arr,1,0,n-1)

    def build(self,t,arr,node,l,r):
        # [l,r] represents the interval (in arr) represented by the node in tree t.
        if(l==r):
            t[node] = arr[l]
            return
        
        m = l+(r-l)//2
        self.build(t,arr,2*node,l,m)
        self.build(t,arr,2*node+1,m+1,r)
        t[node] = min(t[2*node],t[2*node + 1])

    def _update(self,t,node,l,r,idx,val):
        if(l==r):
            t[node] = val
            return
        
        m = l + (r-l)//2
        if(idx<=m):
            self._update(t,node*2,l,m,idx,val)
        else:
            self._update(t,node*2+1,m+1,r,idx,val)
        
        t[node] = min(t[2*node],t[2*node + 1])

    def update(self,idx,val):
        self._update(self.tree,1,0,self.size-1,idx,val)

    def _query(self,t,node,tl,tr,ql,qr):
        # [tl,tr] represents the interval (in arr) represented by the node in tree t.
        # [ql,qr] represents the query interval

        #Interval represented by node is completely outside the given interval of [ql,qr]
        if(tl>qr or tr<ql):
            return float('inf')
        
        #Interval represented by node is completely inside the given interval of [ql,qr]
        if(ql<=tl and tr<=qr):
            return t[node]
        
        #Interval represented by node is partially inside and partially outside the given interval of [ql,qr]
        m = tl + (tr-tl)//2
        lt = self._query(t,node*2,tl,m,ql,qr)
        rt = self._query(t,node*2+1,m+1,tr,ql,qr)
        return min(lt,rt)
    
    def queryMin(self,ql,qr):
        return self._query(self.tree,1,0,self.size-1,ql,qr)