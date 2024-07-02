class SegmentTreeIterative(object):
    def __init__(self, N, update_fn, query_fn,arr):
        #update_fn:max,min,sum
        self.N = N
        self.H = 1
        while 1 << self.H < N:
            self.H += 1
        print(self.H)
        self.update_fn = update_fn
        self.query_fn = query_fn
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N
        self.__build__(arr)

    def __build__(self,arr):
        for i in range(self.N):
            self.tree[i+self.N] = arr[i]
        
        for i in range(self.N-1,0,-1):
            self.tree[i] = self.query_fn(self.tree[2*i], self.tree[2*i+1])

    def _apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    #pull up
    def _pull(self, x):
        while x > 1:
            x //= 2
            self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2 + 1])
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

    #push down
    def _push(self, x):
        for h in range(self.H, 0, -1):
            y = x >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2+ 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, L, R, h):
        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1:
                self._apply(L, h)
                L += 1
            if R & 1 == 0:
                self._apply(R, h)
                R -= 1
            L //= 2; R //= 2
        self._pull(L0)
        self._pull(R0)

    def query(self, L, R):
        L += self.N
        R += self.N
        self._push(L); self._push(R)
        ans = 0
        while L <= R:
            if L & 1:
                ans = self.query_fn(ans, self.tree[L])
                L += 1
            if R & 1 == 0:
                ans = self.query_fn(ans, self.tree[R])
                R -= 1
            L //= 2; R //= 2
        return ans

def addFunc(x,y):
    return x+y

print("\nRange Sum:")
# Range Sum

arr = [1,2,3,4,5,6,7,8,9]
n= len(arr)
#st = SegmentTreeIterative(n, addFunc, lambda x,y:x+y, arr)

st = SegmentTreeIterative(n, addFunc, max, arr)

#print(st)
st.update(0,5,2)
st.update(3,3,10)
st.update(7,8,-1)
print(st.query(0,8))