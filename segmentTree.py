from sortedcontainers import SortedList

class SegmentTree(object):
    def __init__(self,arr):
        n = len(arr)
        self.tree = [0 for i in range(2*n+1)]
        self.size = n
        self.build(arr)

    def build(self, arr):
        for i in range(self.size):
            self.tree[i + self.size] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]
            
    def update(self,idx,val):
        idx += self.size
        self.tree[idx] += val
        while(idx>1):
            parentIdx = idx//2
            self.tree[parentIdx] = self.tree[parentIdx*2] + self.tree[parentIdx*2 + 1]
            idx = parentIdx
    
    def queryRangeSum(self,left,right):
        #query range sum
        result = 0
        left += self.size
        right += self.size
        while(left<=right):
            if(left%2 ==1 ):
                result += self.tree[left]
                left +=1
            
            left = left//2

            if(right%2 == 0):
                result += self.tree[right]
                right -=1
            
            right = right//2
        
        return result
    
    def queryMax(self, l, r):

        l += self.size
        r += self.size 
        ans = float('-inf')
        while l <= r:
            #print(l, r)
            if(l%2):
                ans = max(ans, self.tree[l])
                l += 1
            if(r%2==0):
                ans = max(ans, self.tree[r])
                r -= 1                
            l //= 2
            r //= 2
        return ans

class SegmentTreeMax(object):
    def __init__(self, arr):
        n = len(arr)
        self.size = n
        self.tree = [float('-inf')] * (2*n + 1)
        self.build(arr)
    def build(self, arr):
        for i in range(self.size):
            self.tree[i + self.size] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[2*i],self.tree[2*i + 1])

    def update(self, idx, val):
        idx += self.size
        self.tree[idx] = val
        while idx > 1:
            parentIdx = idx//2
            self.tree[parentIdx] = max(self.tree[parentIdx*2], self.tree[parentIdx*2 +1])
            idx = parentIdx

    def query(self, l, r):

        l += self.size
        r += self.size 
        ans = float('-inf')
        while l <= r:
            #print(l, r)
            if(l%2):
                ans = max(ans, self.tree[l])
                l += 1
            if(r%2==0):
                ans = max(ans, self.tree[r])
                r -= 1                
            l //= 2
            r //= 2
        return ans

class SegmentTreeMin(object):
    def __init__(self, arr):
        n = len(arr)
        self.size = n
        self.tree = [float('inf')] * (2*n + 1)
        self.build(arr)

    def build(self, arr):
        for i in range(self.size):
            self.tree[i + self.size] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = min(self.tree[2*i],self.tree[2*i + 1])

    def update(self, idx, val):
        idx += self.size
        self.tree[idx] = val
        while idx > 1:
            parentIdx = idx//2
            self.tree[parentIdx] = min(self.tree[parentIdx*2], self.tree[parentIdx*2 +1])
            idx = parentIdx

    def query(self, l, r):

        l += self.size
        r += self.size 
        ans = float('inf')
        while l <= r:
            #print(l, r)
            if(l%2):
                ans = min(ans, self.tree[l])
                l += 1
            if(r%2==0):
                ans = min(ans, self.tree[r])
                r -= 1                
            l //= 2
            r //= 2
        return ans