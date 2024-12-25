class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self,data):
        if data not in self.graph:
            self.graph[data] = []

    def add_edge(self,a,b):
        if a not in self.graph:
            self.graph[a] = []
        if b not in self.graph:
            self.graph[b] = []
        self.graph[a].append(b) 
        self.graph[b].append(a)

    def remove_edge(self,a,b):
        if a in self.graph and b in self.graph:
            self.graph[a].remove(b)
            self.graph[b].remove(a)
        
    def remove_vertex(self,a):
        if a in self.graph:
            for i in self.graph:
                if a in self.graph[i]:
                    self.graph[i].remove(a)
            del self.graph[a]

    def search_edge(self,a,b):
        if a in self.graph and b in self.graph:
            if b in self.graph[a]:
                return True
            else :
                return False
                

    def bfs(self,a,end):
        visited = set()
        q = []
        q.append(a)
        visited.add(a)
        print(a)
        while q:
            vertex = q.pop(0)
            if vertex == end:
                return visited
            for i in self.graph[vertex]:
                if i not in visited:
                    print(i)
                    visited.add(i)
                    q.append(i)
        return visited
    
    def dfs(self,a,visited=[]):
        visited.append(a)
        print(a,end=" ")
       
        for i in self.graph[a]:
            if i not in visited:
                self.dfs(i,visited)


    
                   
    # def dfs(self, start_vertex, visited=None):
    #     if visited is None: 
    #         visited = set()

    #     visited.add(start_vertex)
    #     print(start_vertex, end=" ")

    #     for neighbor in self.graph[start_vertex]:
    #         if neighbor not in visited:
    #             self.dfs(neighbor, visited)    

    def show(self):
        for i,j in self.graph.items():
            print(i,j)
        
obj = Graph()
obj.add_vertex('A')
obj.add_vertex('B')
obj.add_edge('A','B')
obj.add_edge('E','B')
obj.add_edge('C','D')
obj.add_edge('C','A')
# obj.add_edge(6,9)
# obj.add_edge(9,10)
# obj.remove_edge(6,8)
# obj.remove_vertex(4)
# print(obj.search_edge(8,6))
obj.show()
print()
print(obj.bfs('A','E'))
print('fvdf')
print()
obj.dfs('A')