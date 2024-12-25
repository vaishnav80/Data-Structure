class Graph:
    def __init__(self):
        self.graph = {}

    def add(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def remove_vertex(self,vertex):
        if vertex in self.graph:
            # First, remove the vertex from other vertices' adjacency lists
            for other_vertex in self.graph:
                if vertex in self.graph[other_vertex]:
                    self.graph[other_vertex].remove(vertex)

            # Finally, remove the vertex itself from the graph
            del self.graph[vertex]
        
    def display_graph(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

    def dfs(self, start_vertex, visited=None):
        if visited is None: 
            visited = set()

        visited.add(start_vertex)
        print(start_vertex, end=" ")

        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

obj = Graph()
obj.add(6)
obj.add(3)
obj.add(5)
obj.add(1)
obj.add(9)
obj.add_edge(6,3)
obj.add_edge(3,1)
obj.add_edge(9,5)
obj.add_edge(1,9)
obj.add_edge(6,5)
obj.display_graph()
obj.bfs(6)
print()
obj.dfs(6)