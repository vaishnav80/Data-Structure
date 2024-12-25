class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        self._insert(self.root,data)
    
    def _insert(self,node,data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            self._insert(node.left,data)
        if data > node.data :
            if node.right is None:
                node.right = Node(data)
            self._insert(node.right,data)

    def inorder(self):
        if self.root is None:
            return None
        self._inorder(self.root)
    
    def _inorder(self,node):
        if node:
            self._inorder(node.left)
            print(node.data,end=" ")
            self._inorder(node.right)
    
    def lca(self,n1,n2):
        if self.root is None:
            return None
        return self._lca(self.root,n1,n2)
    
    def _lca(self,node,n1,n2):
        if n1<node.data and n2<node.data:
            return self._lca(node.left,n1,n2)
        if n1>node.data and n2 >node.data:
            return self._lca(node.right,n1,n2)
        return node.data
    
    def bst(self):
        if self.root is None:
            return False
        return self._bst(self.root,float('-inf'),float('inf'))
    
    def _bst(self,node,min,max):
        if node is None:
            return True
        if not(min<node.data<max):
            return False
        return (self._bst(node.left,min,node.data) and self._bst(node.right,node.data,max))

obj = Tree()
lst = [5,7,9,3,1,4]
for i in lst:
    obj.insert(i)
obj.inorder()
print(obj.lca(3,9))
print(obj.bst())