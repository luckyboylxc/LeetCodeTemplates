
#Find all occurrences of a finite set of strings in a given search string in linear time!
ALPHABET = 26
class Node:
    def __init__(self):
        self.name = 0
        self.exist = []
        self.fail = None
        self.child = [None] * ALPHABET

class AhoCorasick:
    cnt = 0
    def __init__(self, words):
        self.stateNum = 0
        self.root = self.initialize_trie(words)
        self.build_ac(words)        
        self.print_automaton_info()

    def initialize_trie(self, words):
        root = Node()
        for word in words:
            self.trie_insert(root,word)
        return root
    
    def trie_insert(self,root,word):
        currNode = root
        for char in word:
            c = ord(char) - ord('a')
            if not currNode.child[c]:
                currNode.child[c] = Node()
            currNode = currNode.child[c]
        currNode.exist.append(len(word))
    
    def build_ac(self,P):
        root = self.root
        q = []
        for i in range(ALPHABET):
            if root.child[i]:
                root.child[i].fail = root
                q.append(root.child[i])

        while(q):
            x = q.pop(0)
            for i in range(ALPHABET):
                if x.child[i]:
                    
                    #x--fail-→fafail         x--fail-→fafail
                    #  ↘ⁱ             ==>     ↘ⁱ        ↘ⁱ      
                    #    y                      y--fail--→★
                    
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
                    q.append(y)

    def ac_query(self,T):
        currNode = self.root
        print(T)
        for i, char in enumerate(T):
            c = ord(char) - ord('a')
            while (not currNode.child[c] and currNode.fail):
                currNode = currNode.fail
            if currNode.child[c]:
                currNode = currNode.child[c]
            else:
                continue

            if (len(currNode.exist)):
                for length in currNode.exist:
                    self.print_matching_result(T, i - length + 1, length)
    
    def print_matching_result(self, T, start, length):
        firstStr = " "*start
        lastStr = T[start:start +length]
        outPutStr = firstStr + lastStr
        print(outPutStr)
    
    ########################################################
    #用于debug确认构造完成的状态机的[fail指针]和[exist信息]
    #bfs遍历一遍trie,按顺序给节点命名,同时输出fail指向信息
    ########################################################

    def print_automaton_info(self):
        print("---------------------info----------------------")
        q = []
        q.append(self.root)

        while (q):
            currNode = q.pop(0)
            currNode.name = self.stateNum
            self.stateNum +=1
            if currNode.fail:
                print(f"{currNode.name} --fail--> {currNode.fail.name}, has {len(currNode.exist)} word(s)")
            for i in range(ALPHABET):
                if currNode.child[i]:
                    q.append(currNode.child[i])
        print("---------------------end----------------------")


def main():
    patterns = ["he", "she", "hers", "his"]
    text = "ahishers"
    ac = AhoCorasick(patterns)
    ac.ac_query(text)
    return 0




if __name__ == "__main__":
    main()