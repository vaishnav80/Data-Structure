class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insertrec(self.root,key)

    def _insertrec(self,node,key):

        if key <node.data:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insertrec(node.left,key)
        elif key>node.data:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insertrec(node.right,key)
        
    def inorder(self):
        self._inorderrec(self.root)
        print()
    
    def _inorderrec(self,root):
        if root:
            self._inorderrec(root.left)
            print(root.data,end=" ")
            self._inorderrec(root.right)

    def preorder(self):
        self._preorderrec(self.root)
        print()
    
    def _preorderrec(self,root):
        if root:
            print(root.data,end=" ")
            self._preorderrec(root.left)
            self._preorderrec(root.right)

    def postorder(self):
        self._postorderrec(self.root)

    def _postorderrec(self,root):
        if root :
            self._postorderrec(root.left)
            self._postorderrec(root.right)
            print(root.data,end=" ")

    def contains(self,key):
        return self._containsrec(self.root,key)

    def _containsrec(self,node,key):
        if node is None:
            return False
        if node.data == key:
            return True
        elif key <node.data:
            return self._containsrec(node.left,key)
        else:
            return self._containsrec(node.right,key)
        
    def minvalue(self):
        return self._minval(self.root)
    
    def _minval(self,node):
        while node and node.left:
            node = node.left
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
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            elif node.right is None:
                  return node.left
            succcessor = self._minval(node.right)
            node.data = succcessor
            node.right = self._deletes(node.right,succcessor)

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
        return self._sumofnodes(self.root)
    def _sumofnodes(self,node):
        if node is None:
            return 0
        left = self._sumofnodes(node.left)
        
        right = self._sumofnodes(node.right)
        return node.data+left+right
    
    def count(self):
        return self._counts(self.root)
    
    def _counts(self,node):
        if node is None:
            print('return')
            return 0
        left = self._counts(node.left)
        print(left,'left')
        right = self._counts(node.right)
        print(right,'right')
        return 1+left+right

    def countleaf(self):
        return self._countsleaf(self.root)
    
    def _countsleaf(self,node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        left = self._countsleaf(node.left)
    
        right = self._countsleaf(node.right)
        return left+right
    def height(self):
        return self.heights(self.root)
    
    def heights(self,node):
        if node is None:
            return -1
        left = self.heights(node.left)
        right = self.heights(node.right)
        return max(left,right)+1
    
    def is_bst(self):
        return self._is_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_bst_recursive(self, node, min_val, max_val):
        if node is None:
            return True
        
        if not (min_val < node.data < max_val):
            return False

        return (self._is_bst_recursive(node.left, min_val, node.data) and
                self._is_bst_recursive(node.right, node.data, max_val))
    
    def find_lca(self, n1, n2):
        return self._find_lca_recursive(self.root, n1, n2)

    def _find_lca_recursive(self, node, n1, n2):
        if node is None:
            return None

        # If both n1 and n2 are smaller than node's data, LCA lies in the left subtree
        if n1 < node.data and n2 < node.data:
            return self._find_lca_recursive(node.left, n1, n2)

        # If both n1 and n2 are greater than node's data, LCA lies in the right subtree
        if n1 > node.data and n2 > node.data:
            return self._find_lca_recursive(node.right, n1, n2)

        # If one node is on one side and the other is on the other side, this node is the LCA
        return node.data
    def find_second_highest(self):
        if self.root is None:
            return None  # No elements in the tree
        return self._find_second_highest(self.root,None)

    def _find_second_highest(self, node, parent):
        if node.right:
            return self._find_second_highest(node.right, node)
        
        if parent:  # If we have a parent, we can check the left child
            if node.left:
                return self._find_max(node.left)
            else:
                return parent.data  # Return parent data if no left child

        return None # Return the parent node's data

    def _find_max(self, node):
        while node.right:
            node = node.right
        return node.data
    
    def second(self):
        if self.root is None:
            return None
        return self._seconds(self.root)
    
    def _seconds(self,node):
        if not node.left:
            return node.data
        return self._seconds(node.left)
    
    def sum(self):
        if self.root is None:
            return None
        return self._sums(self.root)
    
    def _sums(self,node):
        if not node:
            return 0
        return node.data+self._sums(node.right)+self._sums(node.left)
    
    def leaf(self):
        if self.root is None:
            return None
        return self._leafs(self.root)
    
    def _leafs(self,node):
        if not node:
            return 0
        
        if node.left is None and node.right is None:
            return 1
        
        return self._leafs(node.left)+self._leafs(node.right)
    
    def height(self):
        if self.root is None:
            return None
        return self._heights(self.root)
    
    def _heights(self,node):
        if not node:
            return -1
   
        left = self._heights(node.left)
       
        right = self._heights(node.right)
        return max(left,right)+1
        

obj = Tree()
lst = [6,8,5,4,7,9,3,2,1]
for i in lst:
    obj.insert(i)

obj.inorder()
# obj.preorder()

# obj.postorder()
# print('\n',obj.contains(3))
# print('\n',obj.minvalue())
# # obj.delete(8)
# print(obj.closest(1.8))
# print(obj.sumofnodes())
# obj.inorder()
# print(obj.count())
# print(obj.countleaf())
# print(obj.height())
# print(obj.is_bst())
# print(obj.find_lca(6,9))
# print(obj.find_second_highest())
print(obj.second(),'second')
# print(obj.sum())
# print(obj.leaf())
# print(obj.height())