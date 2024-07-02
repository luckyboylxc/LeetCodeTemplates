class Trie(object):
    def __init__(self):
        self.root = {} 
        
    def insert(self,word):
        curr = self.root
        for ch in word:
            if(ch not in curr):
                curr[ch] = {}
            curr = curr[ch]
        if('#' not in curr):
            curr['#'] = 0
        curr['#'] +=1
            
    def partialMatch(self,word):
        curr = self.root
        ans = 0
        for ch in word:
            if(ch not in curr):
                break
            curr = curr[ch]
            if('#' in curr):
                ans += curr['#']
                     
        return ans
    
    def exactMatch(self,word):
        curr = self.root
        ans = 0
        flag = True
        for ch in word:
            if(ch not in curr):
                flag = False
                break
            curr = curr[ch]
        
        if(flag and '#' in curr):
            ans = curr['#']                    
        return ans
        
class Node(object):
    __slots__ = 'children','count'
    def __init__(self):
        self.children = [None,None]
        self.count = 0

class TrieDLDL(object):
    def __init__(self):
        self.root = {} 

    def insert(self,word):
        curr = self.root
        for ch in word:
            if(ch not in curr):
                curr[ch] = {}
            curr = curr[ch]
        if('#' in curr):
            curr['#'] +=1
        else:
            curr['#'] = 1
                            
    def query(self,word):
        curr = self.root
        ans = 0
        for ch in word:
            if(ch not in curr):
                break
            curr = curr[ch]
            if('#' in curr):
                ans += curr['#']
    
        return ans
    

class Trie(object):
    HIGH_BIT = 20
    def __init__(self):
        self.root = Node()

    def insert(self,num):
        curr = self.root
        for i in range(Trie.HIGH_BIT-1,-1,-1):
            bit = num>>i & 1
            if(curr.children[bit] is None):
                curr.children[bit] = Node()
            
            curr = curr.children[bit]
            curr.count += 1
    
    def remove(self,num):
        curr = self.root
        for i in range(Trie.HIGH_BIT-1,-1,-1):
            bit = num>>i & 1                
            curr = curr.children[bit]
            curr.count -= 1
            
    def query(self,num):
        curr = self.root  
        ans = 0
        for i in range(Trie.HIGH_BIT-1,-1,-1):
            bit = num>>i & 1
            oppBit = bit^1
            if(curr.children[oppBit] and curr.children[oppBit].count):
                ans |= 1<<i
                curr = curr.children[oppBit]
            else:
                curr = curr.children[bit]
                
        return ans

class TrieDL(object):
    LEN = 48
    def __init__(self):
        self.root = {} 

    def insert(self,num):
        curr = self.root
        for i in range(TrieDL.LEN-1,-1,-1):
            bit = num>>i&1
            if(bit not in curr):
                curr[bit] = {}
                curr[bit]['#'] = 0
            curr = curr[bit]
            curr['#'] += 1    

    def remove(self,num):
        curr = self.root
        for i in range(TrieDL.LEN-1,-1,-1):
            bit = num>>i&1
            curr = curr[bit]
            curr['#'] -= 1     
            
    def query(self,val):
        curr = self.root
        ans = 0
        for i in range(TrieDL.LEN-1,-1,-1):
            bit = val>>i&1
            oppBit = 1 - bit
            if(oppBit in curr and curr[oppBit]['#']>0):
                curr = curr[oppBit]
                ans |= 1<<i
            else:
                if(bit in curr):
                    curr = curr[bit]
                else:
                    break
        return ans