class Graph:
    def __init__(self):
        self.graph = {}
    
    def add(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        
    def add_edge(self,vertex1,vertex2):
        if vertex1 in  self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
    
    def display_graph(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

    def dfs(self,start_vertex,visited = None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex,end=" ")
        for i in self.graph[start_vertex]:
                if i not in visited:
                    self.dfs(i,visited)

    def bfs(self,start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)
        while queue:
            vertex = queue.pop()
            print(vertex,end = " ")
            for i in self.graph[vertex]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        
obj = Graph()
obj.add(6)
obj.add(7)
obj.add_edge(6,7)
obj.display_graph()
obj.bfs(6)
obj.dfs(7)