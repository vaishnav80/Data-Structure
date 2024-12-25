### TREE DS

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
        else:
            self._insert(self.root,data)

    def _insert(self,node,data):
        if data<node.data:
            if node.left is None:
                node.left = Node(data)
            else:
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

    def level(self):
        if self.root is None:
            return None
        self._level(self.root)

    def _level(self,node):
        if node:
            queue = [node]
            while queue:
                cur = queue.pop(0)
                print(cur.data,end = " ")
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)

    def second_smallest(self):
        if self.root is None:
            return None
        self._second_smallest(self.root,parent=None)

    def _second_smallest(self,node,parent):
        if node.left:
            return self._second_smallest(node.left,node)
        if node.right is not None:
            return self._min(node.right).data
        if parent:
            return parent.data
    
    def min(self):
        if self.root is None:
            return None
        self._min(self.root)
    
    def _min(self,node):
        
        while node:
            node = node.right
        return node
    
    def delete(self,data):
        if self.root is None:
            return None
        self._delete(self.root,data)
    
    def _delete(self,node,data):
        if data <node.data:
            node.left = self._delete(node.left,data)
        elif data > node.data :
            node.right = self._delete(node.right,data)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left 
            successor = self._min(node.right)
            node.data = successor
            node.data = self._delete(node.right,successor)
        return node
        
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

obj = Tree()
lst = [10,6,5,8,16,13,12,14,3,9]
for i in lst:
    obj.insert(i)

obj.level()
print(obj.second_smallest(),'dddddd')
obj.inorder()
print()
obj.delete(12)
obj.inorder()
print(obj.height())
print('f')





##      HEAP ###

class Heap:
    def __init__(self):
        self.heap = []
    
    def insert(self,data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)
    
    def heapify_up(self,n):
        parent= (n-1)//2
        if n>0 and self.heap[parent] < self.heap[n]:
            self.heap[parent],self.heap[n] = self.heap[n],self.heap[parent]
            self.heapify_up(parent)
    
    def extract(self):
        temp = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_d(0)
        return temp
    
    def heapify_d(self,n):
        left = 2*n+1
        right = 2*n+2
        largest = n
        if left<len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != n:
            self.heap[n],self.heap[largest] = self.heap[largest],self.heap[n]
            self.heapify_d(largest)

    def sort(self):
        n= len(self.heap)
        for i in range(n-1,-1,-1):
            self.heapify_down(i,n)

        for i in range(n-1,-1,-1):
            self.heap[0],self.heap[i] = self.heap[i],self.heap[0]
            self.heapify_down(0,i)
    def heapify_down(self,i,n):
        left = 2*i+1
        right = 2*i+2
        largest = i
        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest !=i:
            self.heap[largest],self.heap[i] = self.heap[i],self.heap[largest]
            self.heapify_down(largest,n)


    def display(self):
        print(self.heap)

heap = Heap()
lst2 = [10,6,5,8,16,13,12,14,3,9]
for i in lst:
    heap.insert(i)

print()
heap.display()
heap.extract()
heap.display()
heap.sort()

heap.display()


## TRIE  ##

class TrieNode :

    def __init__(self):
        self.children = {}
        self.end = False
    

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.end = True


    def display(self,node = None,word = " ",new = None):
        if node is None:
            node = self.root
        if new is None:
            new = []
        if node.end:
            new.append(word)
        
        for k,v in node.children.items():
            self.display(v,word +k,new)
        
        return new
    
    def prefix(self,word):

        def prefix_word(node,word,new):

            if node.end :
                new.append(word)
            for k,v in node.children.items():
                prefix_word(v,word+k,new)
            
            return new

        node = self.root
        new = []
        for i in word:
            if i not in node.children:
                return []
            node = node.children[i]
        
        return prefix_word(node,word,new)

trie = Trie()
trie.insert('hello')
trie.insert('hai')
print(trie.prefix('ha'))
print(trie.display())


## GRAPH ##

class Graph:
    def __init__(self):
        self.graph = {}

    def add(self,v1):
        if v1  not in self.graph:
            self.graph[v1] ={}

    def add_edge(self,v1,v2,w):
        if v1 not in self.graph:
            self.graph[v1] = {}
        if v2 not in self.graph:
            self.graph[v2] = {}
        self.graph[v1][v2] = w

    def dfs(self,v1,visited=None):
        
        if visited is None:
            visited = []
        visited.append(v1)
        for i in  self.graph[v1]:
            if i not in visited:
                self.dfs(i,visited)
        return visited
    
    def bfs(self,v1):
        queue = [v1]
        visited = [v1]
        while queue:
            curr = queue.pop(0)
            for i in self.graph[curr]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
        return visited
    
    def dijkstras(self,start,end):
        queue = [(0,start)]
        distances = {vertex : float('inf') for vertex in self.graph}
        previous = {vertex : None for vertex in self.graph}

        while queue:
            curr_distance,curr_vertex = queue.pop(0)
            for k,v in self.graph[curr_vertex].items():
                distance = curr_distance+v
                if distance<distances[k]:
                    distances[k] = distance
                    previous[k] = curr_vertex
                    queue.append((distance,k))
        
        path= []
        curr = end
        while curr:
            path.insert(0,curr)
            curr = previous[curr]
        
        return path,distances[end]
    
    def dijkstra(self,start,end):
        queue = [(0,start)]
        distances = {vertex : float('inf') for vertex in self.graph}
        previous = {vertex : None for vertex in self.graph}
        while queue:
            cur_distance,cur_vertex = queue.pop(0)
            for k,v in self.graph[cur_vertex].items():

                distance = cur_distance+v
                if distance < distances[k]:
                    distances[k] = distance
                    previous[k] = cur_vertex
                    queue.append((distance,k))
        
        path = []
        currrent = end
        while currrent:
            path.insert(0,currrent)
            currrent = previous[currrent]
        
        return path,distances[end]
    
                
    

    
    def display(self):
        print(self.graph)

    
graph = Graph()
graph.add(5)
graph.add(8)
graph.add_edge(5,8,3)
graph.add_edge(5,6,7)
graph.add_edge(6,10,2)
graph.add_edge(8,10,12)
print(graph.bfs(5))
print(graph.dfs(5))
print(graph.dijkstra(5,10))
graph.display()
