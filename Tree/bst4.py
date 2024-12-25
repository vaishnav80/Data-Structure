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
        self._insert_rec(self.root,data)
    
    def _insert_rec(self,node,data):

        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            self._insert_rec(node.left,data)
        if data > node.data:
            if node.right is None:
                node.right = Node(data)
            self._insert_rec(node.right,data)

    def inorder(self):

        if self.root is None:
            return None
        self._inorder_rec(self.root)
    
    def _inorder_rec(self,node):
        if node:
            self._inorder_rec(node.left)
            print(node.data,end=" ")
            self._inorder_rec(node.right)

    def preorder(self):
        if self.root is None:
            return None
        self._preorder_rec(self.root)
    
    def _preorder_rec(self,node):
        if node:
            print(node.data,end=" ")
            self._preorder_rec(node.left)
            self._preorder_rec(node.right)

    def postorder(self):
        if self.root is None:
            return None
        self._postorder_rec(self.root)
    
    def _postorder_rec(self,node):
        if node:
            self._postorder_rec(node.left)
            self._postorder_rec(node.right)
            print(node.data,end=" ")

    def min(self):
        if self.root is None:
            return None
        return self._min(self.root)
    
    def _min(self,node):
        while node.left:
            node = node.left
        return node.data

    def max(self):
        if self.root is None:
            return None
        return self._max(self.root)
    
    def _max(self,node):
        while node.right:
            node = node.right
        return node.data
    
    def delete(self,key):
        self.root = self._deletes(self.root,key)
    
    def _deletes(self,node,key):
        if node is None:
            return node
        if key<node.data:
            node.left = self._deletes(node.left,key)
        elif key>node.data:
            node.right = self._deletes(node.right,key)
        else:
            node.right,succcessor

        return node

obj = Tree()
list1 = [8,3,1,6,4,7,10,14,13]
for i in list1:
    obj.insert(i)

obj.inorder()
print()
obj.preorder()
print()
obj.postorder()
print()
# print(obj.min())
# print(obj.max())
# obj.delete(7)
# obj.inorder()