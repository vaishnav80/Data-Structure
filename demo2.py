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
            self.root  = Node(data)
        self._insert(self.root,data)
    
    def _insert(self,node,data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            self._insert(node.left,data)
        
        if data>node.data:
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

    def leaf(self):
        if self.root is None:
            return None
        return self._leaf(self.root)

    def _leaf(self,node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._leaf(node.left)+self._leaf(node.right)
    
    def sum(self):
        if self.root is None:
            return None
        return self._sum(self.root)
    
    def _sum(self,node):
        if node is None:
            return 0
        return node.data+self._sum(node.left)+self._sum(node.right)
    
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
    
    def second_s(self):
        if self.root is None:
            return None
        return self._second_s(self.root,parent=None)

    def _second_s(self,node,parent):
        if node.left :
            return self._second_s(node.left,node)
        if node.right:
            return self._min(node.right)
        return parent.data
    
    def min(self):
        if self.root is None:
            return None
        self._min(self.root)

    def _min(self,node):
        while node.left:
            node = node.left
        return node.data
    def second_l(self):
        if self.root is None:
            return None
        return self._second_l(self.root,parent=None)

    def _second_l(self,node,parent):
        if node.right :
            return self._second_l(node.right,node)
        if node.left:
            return self._max(node.left)
        return parent.data
    
    def max(self):
        if self.root is None:
            return None
        self._max(self.root)

    def _max(self,node):
        while node.right:
            node = node.right
        return node.data
    
    def delete(self,second):
        if self.root is None:
            return None
        self.root = self._delete(self.root,second)

    def _delete(self,node,second):
        # if node is None:
        #     return node
        if second < node.data:
            node.left =  self._delete(node.left,second)
        
        elif second> node.data:
            node.right =  self._delete(node.right,second)

        else:
            # if node.left is None and node.right is None:
            #     return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succe = self._min(node.right)
            node.data = succe
            self._delete(node.right,succe)
            
        return node

    
    


obj = Tree()
lst = [10,6,8,9,1,5,4]   
for i in lst:
    obj.insert(i)
obj.inorder()  
print(obj.leaf())   
print(obj.sum()) 
print(obj.height())   
print(obj.second_s())
second = obj.second_s()
print(obj.second_l())
obj.delete(second)
obj.inorder()  




class TrieNode2:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Trie2:
    def __init__(self):
        self.root  = TrieNode2()
    
    def insert(self,word):
        node = self.root
        for i in word :
            if i not in node.children:
                node.children[i] = TrieNode2()
            node = node.children[i]
        node.end = True
    
    def collect(self,node = None,word = "" ,new = None):
        if node is None:
            node = self.root
        if new is None:
            new = []
        if node.end:
            new.append(word)
        for k,v in node.children.items():
            self.collect(v,word+k,new)
        return new

trie2 = Trie2()
trie2.insert('hello')
trie2.insert('hai')
print(trie2.collect())

