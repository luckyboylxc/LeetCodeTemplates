#Find all occurrences of a finite set of strings in a given search string in linear time!

class node:
    def __init__(self):
        self.fail = 0
        self.child = [0 for i in range(26)]
        self.exist = []
        

tot = 0
trie = [node() for i in range(1000)]


def insert(str):
    global tot
    u = 0
    for c in str:
        id = ord(c) - ord('a')
        if trie[u].child[id] == 0:
            tot += 1
            trie[u].child[id] = tot
        u = trie[u].child[id]
    trie[u].exist.append(len(str))


def build():
    q = []
    for i in range(26):
        if trie[0].child[i]:
            q.append(trie[0].child[i])
    while q:
        u = q[0]
        q.pop(0)
        for i in range(26):
            if trie[u].child[i]:
                trie[trie[u].child[i]].fail = trie[trie[u].fail].child[i]
                q.append(trie[u].child[i])
            else:
                trie[u].child[i] = trie[trie[u].fail].child[i]


def query(str):
    u = 0
    res = []
    for i in range(len(str)):
        c = str[i]
        j = u = trie[u].child[ord(c) - ord('a')]
        while j and trie[j].exist:
            for k in trie[j].exist:
                res.append((i - k + 1, str[i - k + 1: i + 1]))
            j = trie[j].fail
    print(res)

if __name__ == "__main__":
    insert('he')
    insert('she')
    insert('his')
    insert('hers')
    build()
    query('ahishers')