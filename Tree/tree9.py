class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root= None
    # def insert(self,data):
    #     if self.root is None:
    #         self.root = Node(data)
    #     else:
    #         self._insert(self.root,data)
    
    # def _insert(self, node, data):
    #     queue = [node]  
    #     while queue:
    #         current = queue.pop(0) 
    #         print(current.data)
    #         if current.left is None:
    #             current.left = Node(data)
    #             return
    #         else:
    #             queue.append(current.left)

    #         if current.right is None:
    #             current.right = Node(data)
    #             return
    #         else:
    #             queue.append(current.right)
    
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)
    
    def _insert(self,node,data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            self._insert(node.left,data)
        if data > node.data:
            if node.right is None:
                node.right = Node(data)
            self._insert(node.right,data)
    def inorder(self):
        if self.root is None:
            return None
        self.inorder_traversal(self.root)

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def bst(self):

        if self.root is None:
             return False
        return self._bst(self.root,float('-inf'),float('inf'))
    
    def _bst(self,node,min,max):
        if node is None :
            return True
        if not (min<node.data<max):
            return False
        return (self._bst(node.left,min,node.data) and self._bst(node.right,node.data,max)) 

    def levelorder(self):
        if self.root is None:
            return None
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            print(cur.data,end=" ")
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

    def lca(self,n1,n2):
        if self.root is None:
            return None
        return self._lca(self.root,n1,n2)
    
    def _lca(self,node,n1,n2):
        if n1<node.data and n2<node.data:
            return self._lca(node.left,n1,n2)
        elif n1>node.data and n2>node.data:
            return self._lca(node.right,n1,n2)
        return node.data

obj = Tree()
lst = [5,4,6,9,7,10]
for i in lst:
    obj.insert(i)
obj.inorder()
print(obj.bst())
obj.levelorder()
print()
print(obj.lca(7,10))