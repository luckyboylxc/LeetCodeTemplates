from queue import Queue

ALPHABET = 26
cnt = 0
class Node:
    def __init__(self):
        self.name = 0
        self.exist = []
        self.fail = None
        self.child = [None] * ALPHABET

def print_matching_result(T, start, length):
    for i in range(start):
        print(" ", end="")
    for i in range(length):
        print(T[start + i], end="")
    print()

def print_automaton_info(root):
    print("---------------------info----------------------")
    q = Queue()
    q.put(root)
    while not q.empty():
        tmp = q.get()
        tmp.name = cnt
        if tmp.fail:
            print(f"{tmp.name} --fail--> {tmp.fail.name}, has {len(tmp.exist)} word(s)")
        for i in range(ALPHABET):
            if tmp.child[i]:
                q.put(tmp.child[i])
    print("---------------------end----------------------")

def trie_insert(root, word):
    tmp = root
    for char in word:
        c = ord(char) - ord('a')
        if not tmp.child[c]:
            tmp.child[c] = Node()
        tmp = tmp.child[c]
    tmp.exist.append(len(word))

def ac_build(root, P):
    for pattern in P:
        trie_insert(root, pattern)

    q = Queue()
    for i in range(ALPHABET):
        if root.child[i]:
            root.child[i].fail = root
            q.put(root.child[i])

    while not q.empty():
        x = q.get()
        for i in range(ALPHABET):
            if x.child[i]:
                y = x.child[i]
                fafail = x.fail
                while fafail and not fafail.child[i]:
                    fafail = fafail.fail
                if not fafail:
                    y.fail = root
                else:
                    y.fail = fafail.child[i]

                if y.fail.exist:
                    y.exist.extend(y.fail.exist)
                q.put(y)

def ac_query(root, T):
    tmp = root
    for i, char in enumerate(T):
        c = ord(char) - ord('a')
        while (not tmp.child[c] and tmp.fail):
            tmp = tmp.fail
        if tmp.child[c]:
            tmp = tmp.child[c]
        else:
            continue

        if (len(tmp.exist)):
            for length in tmp.exist:
                print_matching_result(T, i - length + 1, length)

def aho_corasick(P, T):
    print("**********************************************")
    print(" ".join(f'"{pattern}"' for pattern in P))
    print(T)

    root = Node()
    ac_build(root, P)
    ac_query(root, T)

    print_automaton_info(root)

# Example usage:
patterns = ["he", "she", "hers", "his"]
text = "ahishers"
aho_corasick(patterns, text)