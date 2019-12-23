import random

class BSTNode():

    def __init__ (self,data):
        self.data = data
        self.count = 1
        self.left = None
        self.right = None


class BST():

    def __init__ (self):
        self.root = None

    def insert (self,data):

        #print ("adding: ",data)
        if self.root is None:
            self.root = BSTNode(data)
            return

        #print ("root left #1 ",self.root.left)
        #print ("root right #1 ",self.root.right)
        self._insert(self.root,data)
        #print ("root left #2 ",self.root.left)
        #print ("root right #2 ",self.root.right)


    def _insert (self,node,data):

        if data == node.data:
            node.count += 1
        elif data <= node.data:
            if node.left is None:
                node.left = BSTNode(data)
            else:
                self._insert(node.left,data)

        elif data > node.data:
            if node.right is None:
                node.right = BSTNode(data)
            else:
                self._insert(node.right,data)

    def inorder (self):
        self._inorder (self.root)
        print ("")

    def _inorder (self,node):
        if node is None:
            return
        self._inorder(node.left)
        print (node.data,"(%d)" % (node.count),end=' ')
        self._inorder(node.right)


    def search (self,data):
        #print ("search...")
        return self._search(self.root,data)

    def _search (self,node,data):
        #print ("   >search...")
        if node is None:
            return False

        if node.data == data:
            return True

        if data <= node.data:
            return self._search(node.left,data)
        else:
            return self._search(node.right,data)

    def maxdepth(self):
        return self._maxdepth(self.root)

    def _maxdepth(self,node):
        if node is None:
            return 0
        l = self._maxdepth(node.left)
        r = self._maxdepth(node.right)

        return 1 + max(l,r)


if __name__ == "__main__":

    bst = BST()
    bst.insert (15)
    bst.insert (10)
    bst.insert (20)
    bst.insert (25)
    bst.insert (8)
    bst.insert (12)
    bst.insert (6)
    bst.insert (9)
    bst.insert (25)
    bst.insert (9)
    bst.insert (9)

#          15
#      10      20
#    8    12        25
#   6 9
#

    print ("in order: ")
    bst.inorder()

    print ("searching for 15 : ",bst.search(15))
    print ("searching for 51 : ",bst.search(51))
    print ("searching for 8 : ",bst.search(8))
    print ("searching for 12 : ",bst.search(12))

    print ("inserindo 1 milhão de numeros...")
    bst2 = BST()
    for n in range(1,1000000):
        bst2.insert(random.randint(1,10000000))

    print ("searching for 42342",bst2.search(42342))
    print ("searching for 512342",bst2.search(512342))
    print ("searching for 565534",bst2.search(565534))
    print ("in order: ")
    #bst2.inorder()
    print("Max depth: ",bst2.maxdepth())
