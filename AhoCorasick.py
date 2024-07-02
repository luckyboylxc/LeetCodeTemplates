#Find all occurrences of a finite set of strings in a given search string in linear time!

from collections import deque
class TrieNode():
    def __init__(self):
        self.next = {}
        self.terminal = False
        self.fail = None

class AhoCorasick:

    def __init__(self, words: List[str]):
        self.trie = self.initialize_trie(words)
        self.root = self.trie
        self.build_ac_automaton()
        self.current = self.trie
                
    def initialize_trie(self, words):
        trie = TrieNode()
        for word in words:
            cur = trie
            for c in word:
                if c not in cur.next:
                    cur.next[c] = TrieNode()
                cur = cur.next[c]
            cur.terminal = True
            # cur.word = word
        return trie
    
    def build_ac_automaton(self): #make fail pointer
        q = deque([self.trie]) 
        while q:
            cur = q.popleft()
            p = None
            for key,value in cur.next.items():
                if cur == self.root:
                    value.fail = self.root
                else:
                    p = cur.fail
                    while p is not None:
                        if key in p.next:
                            value.fail = p.next[key]
                            if p.next[key].terminal == True:
                                value.terminal = True
                            break
                        p = p.fail
                    if p is None:
                        value.fail = self.root
                q.append(value)
