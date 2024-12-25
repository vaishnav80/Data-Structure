class Node:

    def __init__(self,data):
        self.data = data
        self.left= None
        self.right = None
    
class tree:
    def __init__(self):
        self.root = None
    
    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        self._insert(self.root,key)

    def _insert(self,node,key):
        if key < node.data:
            if node.left is None:
                node.left = Node(key)
            self._insert(node.left,key)

        elif key>node.data:
            if node.right is None:
                node.right = Node(key)
            self._insert(node.right,key)
            

    def inorder(self):
        if self.root is None:
            return None
        self._inorder(self.root)
    def _inorder(self,node):
        if node:
            self._inorder(node.left)
            print(node.data,end = " ")
            self._inorder(node.right)
    def contains(self,key):
        return self._contains(self.root,key)
    
    def _contains(self,node,key):
        if node is None:
            return False
        if node.data == key:
            return True
        if key<node.data:
            return self._contains(node.left,key)
        if key>node.data:
            return self._contains(node.right,key)
        
    def minvalue(self):
        if self.root is None:
            return None
        return self._min(self.root)
    
    def _min(self,node):
        while node and node.left:
            node = node.left
        return node.data
    def _max(self,node):
        while node and node.right:
            node = node.right
        return node.data
    
    def delete(self,key):
        self._delete(self.root,key)
    
    def _delete(self,node,key):
        if node is None:
            return node
        if key < node.data:
            node.left = self._delete(node.left,key)
        elif key>node.data:
            node.right = self._delete(node.right,key)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            succcessor = self._min(node.right)
            node.data = succcessor
            node.right = self._delete(node.right,succcessor)

        return node
    def closest(self,key):
        return self._closests(self.root,key,float('inf'))
    def _closests(self,node,key,closest):
        if node is None:
            return closest
        if abs(node.data - key) < abs(closest - key):
            closest = node.data

        if key < node.data:
            return self._closests(node.left, key, closest)
        elif key > node.data:
            return self._closests(node.right, key, closest)
        else:
            return closest 
        
    
    def sumofnodes(self):
        if self.root is None:
            return None
        return self._sumofnodes(self.root)
    
    def _sumofnodes(self,node):
        if node is None:
            return 0
        return node.data+self._sumofnodes(node.left)+self._sumofnodes(node.right)
    
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
        if not node:
            return 0
        if node.left is None or node.right is None:
            return 1
        return self._countleaf(node.left)+self._countleaf(node.right)
    
    def height(self):
        if self.root is None:
            return -1
        return self._height(self.root)
    
    def _height(self,node):
        if not node :
            return -1
        left =  self._height(node.left)
        
        right =  self._height(node.right)
        return max(left,right)+1
    
    def is_bst(self):
        if self.root is None:
            return True
        return self._is_bst(self.root,float('-inf'),float('inf'))
    
    def _is_bst(self,node,min_val,max_val):
        
        if node is None:
            return True
        if not (min_val < node.data < max_val):
            return False

        return (self._is_bst(node.left, min_val, node.data) and
                self._is_bst(node.right, node.data, max_val))
    
    def find_second_highest(self):
        if self.root is None:
            return None
        return self._find_second_highest(self.root,None)
    
    def _find_second_highest(self,node,parent):
        if node.right:
            return self._find_second_highest(node.right,node)
        if parent and node.left:
            return self._max(node.left)
        return parent.data
    
    def find_second_smallest(self):
        if self.root is None:
            return None
        return self._find_second_smallest(self.root,None)
    
    def _find_second_smallest(self,node,parent):
        if node.left:
            return self._find_second_smallest(node.left,node)
        if parent and node.right:
            return self._min(node.right)
        return parent.data
        
        


obj = tree()
lst = [6,8,5,4,7,9,3,2,1]
for i in lst:
    obj.insert(i)

obj.inorder()
# obj.preorder()

# obj.postorder()
print('\n',obj.contains(3),'c')
print('\n',obj.minvalue())
# obj.delete(8)
# print(obj.closest(1.8),'clo')
print(obj.sumofnodes())
obj.inorder()
print()
print(obj.count())
print(obj.countleaf())
print(obj.height())
# print(obj.is_bst())
# print(obj.find_lca(6,9))
print(obj.find_second_highest(),'highest')
print(obj.find_second_smallest(),'second')
# print(obj.sum())
# print(obj.leaf())
# print(obj.height())