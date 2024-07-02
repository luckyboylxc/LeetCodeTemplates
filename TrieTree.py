class TrieNode:
    __slots__ = 'children','isWord'
    def __init__(self, isWord = False):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = isWord

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.isWord

