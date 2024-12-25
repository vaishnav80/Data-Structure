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
        if data < node.data :
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
            curr = queue.pop(0)
            print(curr.data,end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

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
            
    def delete(self,data):
        if self.root is None:
            return None
        self._delete(self.root,data)
    
    def _delete(self,node,data):
        if node is None:
            return None
        if data<node.data:
            node.left = self._delete(node.left,data)
        elif data>node.data:
            node.right = self._delete(node.right,data)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            successor = self._min(node.right)
            node.data = successor
            node.right = self._delete(node.right,successor)
        return node

    def sum(self):
        if self.root is None:
            return None
        return self._sum(self.root)
    
    def _sum(self,node):
        if node is None:
            return 0
        return node.data+self._sum(node.left)+self._sum(node.right)
    
    def count(self):
        if self.root is None:
            return None
        return self._count(self.root)
    
    def _count(self,node):
        if node is None:
            return 0
        return self._count(node.left)+self._count(node.right)+1
    
    def countleaf(self):
        if self.root is None:
            return None
        return self._countleaf(self.root)
    
    def _countleaf(self,node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._countleaf(node.left)+self._countleaf(node.right)
    def height(self):
        if self.root is None:
            return None
        return self._height(self.root)
    
    def _height(self,node):
        if node is None:
            return -1
        left = self._height(node.left)
        right = self._height(node.right)
        return max(left,right)+1
    
    def second_largest(self):
        if self.root is None:
            return None
        s_l = self._second_largest(self.root,None)
        s_s = self._second_smallest(self.root,None)
        return s_l+s_s

    def _second_largest(self,node,parent):
        if node.right:
            return self._second_largest(node.right,node)
        if node.left:
            return self._max(node.left)
        else:
            return parent.data
        
    def _second_smallest(self,node,parent):
        if node.left:
            return self._second_smallest(node.left,node)
        if node.right:
            return self._min(node.right)
        return parent.data
        
    def searching(self,data):
        if self.root is None:
            return None
        return self._searching(self.root,data)

    def _searching(self,node,data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._searching(node.left,data)
        else:
            return self._searching(node.right,data)

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
    
    def lca(self,n1,n2):
        if self.root is None:
            return None
        return self._lca(self.root,n1,n2)
    
    def _lca(self,node,n1,n2):
        if node is None:
            return None
        if n1 <node.data and n2<node.data:
            return self._lca(node.left,n1,n2)
        if n1 > node.data and n2>node.data:
            return self._lca(node.right,n1,n2)
        return node.data
    
    def closest(self,key):
        if self.root is None:
            return None
        
        return self._closest(self.root,key,closest = self.root.data)
    
    def _closest(self,node,key,closest):
        if node is None:
            return closest
        
        if abs(node.data - key) < abs (closest - key):
            closest = node.data

        if key < node.data : 
            return self._closest(node.left,key,closest)
        
        if key > node.data:
            return self._closest(node.right,key,closest)

        return closest

obj = Tree()
lst = [10,5,2,7,1,3,6,8,15,11,19]
for i in lst:
    obj.insert(i)
obj.inorder()
print()
obj.postorder()
print()
obj.preorder()
print()
obj.levelorder()
print('\n',obj.min())
print(obj.max())
# obj.delete(7)
obj.inorder()
print() 
print(obj.sum())
print(obj.count())
print(obj.countleaf())
print(obj.height())
print('sum',obj.second_largest())
# print(obj.searching(2))
print(obj.bst())
print(obj.lca(3,19))
print(obj.closest(25))