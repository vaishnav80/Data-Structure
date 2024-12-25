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

        if data > node.data:
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

    def preorder(self):
        if self.root is None:
            return None
        self._preorder(self.root)

    def _preorder(self,node):
        if node:
            print(node.data,end=" ")
            self._preorder(node.left)
            self._preorder(node.right)
    
    def postorder(self):
        if self.root is None:
            return None
        self._postorder(self.root)

    def _postorder(self,node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.data,end=" ")

    def levelorder(self):
        queue = []
        queue.append(self.root)
        while queue:
            currnt = queue.pop(0)
            print(currnt.data , end=" ")
            if currnt.left:
                queue.append(currnt.left)
            if currnt.right:
                queue.append(currnt.right)
        
    def sum(self):
        if self.root is None:
            return None
        return self._sum(self.root)
    
    def _sum(self,node):
        if not node:
            return 0
        return node.data+self._sum(node.left)+self._sum(node.right)
    
    def count(self):
        if self.root is None:
            return None
        return self._count(self.root)
    
    def _count(self,node):
        if not node:
            return 0
        return self._count(node.left)+self._count(node.right)+1
    
    def leaf(self):
        if self.root is None:
            return None
        return self._leaf(self.root)
    
    def _leaf(self,node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self._leaf(node.left)+self._leaf(node.right)

obj = Tree()
lst = [9,2,3,6,7,1]
for i in lst:
    obj.insert(i)

obj.inorder()
print()
obj.preorder()      
print()
obj.postorder()
print()
obj.levelorder()
print(obj.sum())
print(obj.count())
print(obj.leaf())