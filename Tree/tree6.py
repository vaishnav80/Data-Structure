class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class Tree :
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
        if self.root is None:
            return None
        self._level(self.root)
    
    def _level(self,node):
        if node:
            queue = [node]
            while queue:
                cur = queue.pop(0)
                print(cur.data,end=" ")
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
    
    def deletion(self,data):
        if self.root is None:
            return None
        self._delete(self.root,data)
    
    def _delete(self,node,data):
        if node is None:
            return None
        if data<node.data:
            node.left = self._delete(node.left,data)
        elif data > node.data:
            node.right = self._delete(node.right,data)
        
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            successor = self._min(node.right)
            node.data = successor
            node.right = self._delete(node.right,successor)
        return node

    def _min(self,node):
        while node.left:
            node = node.left
        return node.data
    
    def min(self):
        if self.root is None:
            return None
        self._min(self.root)
    
    
    def searching(self,data):
        if self.root is None:
            return None
        return self._search(self.root,data)
    
    def _search(self,node,data):
        if node is None:
            return False
        
        if node.data == data:
            return True
        elif data < node.data:
            return self._search(node.left,data)
        else:
            return self._search(node.right,data)
        
        
    
    def closest(self,data):
        if self.root is None:
            return None
        return self._closest(self.root,data,closest = None)
    
    def _closest(self,node,data,closest):
        if node is None:
            return closest
        if closest is None:
            closest = node.data
        if abs(node.data - data) < abs(closest-data):
            closest = node.data
        if data<node.data:
            return self._closest(node.left,data,closest)
        elif data > node.data:
            return self._closest(node.right,data,closest)
        return closest
    
    def bst(self):
        if self.root is None:
            return None
        return self._bst(self.root,min = float('-inf'),max = float('inf'))

    def _bst(self,node,min,max):
        if node is None:
            return True
        
        if not (min<node.data<max):
            return False
        return (self._bst(node.left,min,node.data) and self._bst(node.right,node.data,max)) 

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
            return 0
        return self._count(self.root)
    
    def _count(self,node):
        if node is None:
            return 0
        return self._count(node.left)+self._count(node.right)+1
    
    def count_leaf(self):
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
        
    def lca(self,n1,n2):
        if self.root is None:
            return None
        return self._lca(self.root,n1,n2)
    
    def _lca(self,node,n1,n2):
        if node is None:
            return None
        if n1 < node.data and n2 < node.data:
            return self._lca(node.left,n1,n2)
        if n2> node.data and n1 > node.data:
            return self._lca(node.right,n1,n2)
        return node.data
    
    def second_largest(self):
        if self.root is None:
            return False
        return self._secondlargest(self.root,temp = None)
    
    def _secondlargest(self,node,temp):
        if node.right:
            return self._secondlargest(node.right,node)
        if node.left:
            return self._max(node.left)
        else:
            return temp.data
    def max(self):
        if self.root is None:
            return None
        self._max(self.root)
    
    def _max(self,node):
        while node.right:
            node = node.right
    
    
        return node.data
    
    def second_smallest(self):
        if self.root is None:
            return None
        return self._secondsmallest(self.root,temp = None)

    def _secondsmallest(self,node,temp):
        if node.left:
            return self._secondsmallest(node.left,node)
        if node.right:
            self._min(node.right)
        else:
            return temp.data
lst = [10,15,8,6,3,7,13,17]
obj = Tree()
for i in lst:
    obj.insert(i)

obj.inorder()
print()
obj.postorder()
print()
obj.preorder()
print()
obj.levelorder()
obj.deletion(15)
print()
obj.inorder()
print(obj.searching(13))
print(obj.closest(11))
print(obj.bst())
print(obj.sum())
print(obj.count())
print(obj.count_leaf())
print(obj.height())
print(obj.lca(3,7))
print(obj.second_largest(),'gf')
print(obj.second_smallest())

