from collections import defaultdict

class TrieNode:

    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class Trie:

    def __init__(self):
        self.root = self.new_node()

    def new_node(self):
        return TrieNode()
    
    def get_index(self,ch):
        return ord(ch) - ord('a')

    def insert (self,word):

        curnode = self.root
        lenw = len(word)

        for i in range(lenw):

            index = self.get_index(word[i])

            if index not in curnode.children:
                curnode.children[index] = self.new_node()
            curnode = curnode.children.get(index)

        curnode.terminating = True

    def search (self,word):

        curnode = self.root
        lenw = len(word)

        for i in range(lenw):
            index = self.get_index(word[i])
            if not curnode:
                return False
            curnode = curnode.children.get(index)
            print ("index: ",index, " chr: ",chr(index+ord('a'))," ",curnode.terminating)
        
        return True if curnode and curnode.terminating else False



if __name__ == "__main__":

    strings = ["bye","she","car","shells","shellsort"]

    t = Trie()
    for word in strings:
        t.insert(word)

    print ("searching for: bye " , t.search("bye"))
    print ("searching for: she " , t.search("she"))
    print ("searching for: shells " , t.search("shells"))
    print ("searching for: shellsort " , t.search("shellsort"))
    print ("searching for: shellsortalgo " , t.search("shellsortalgo"))

    