class Graph:
    def __init__(self):
        self.graph = {}

    def add(self,v1):
        if v1 not in self.graph:
            self.graph[v1] = {}

    def add_edge(self,v1,v2,a):
        if v1 not in self.graph:
            self.graph[v1] = {}

        if v2 not in self.graph:
            self.graph[v2] = {}
        
        self.graph[v1][v2] = a

    def display(self):
        print(self.graph)

    def dijikstra(self,start,end):
        queue = [(0,start)]
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        previous = {vertex : None for vertex in self.graph  }

        while queue:
            cur_dis,cur_vertex = queue.pop(0)
            for neighbour,weight in self.graph[cur_vertex].items():
                
                distance = cur_dis + weight
                if distance < distances[neighbour]:
                   
                    distances[neighbour] = distance
                    previous[neighbour] = cur_vertex
                    queue.append((distance,neighbour))

        print(distances,previous)
        path = []
        current = end
        while current:
            path.insert(0,current)
            current = previous[current]
        print(path,distances[end])

    def bfs(self,v1):
        queue = [v1]
        visited = [v1]
        while queue:
            curr  = queue.pop(0)
            for k in self.graph[curr]:
                if k not in visited:
                    visited.append(k)
                    queue.append(k)

        return visited
    
    def dfs(self,v1,visited=None):
        if visited is None:
            visited = []
        
        visited.append(v1)
        for k in self.graph[v1]:
            if k not in visited:
                self.dfs(k,visited)
        return visited
    
        
        


obj  = Graph()
obj.add_edge('a','b',50)
obj.add_edge('a','c',10)
obj.add_edge('b','d',2)
obj.add_edge('c','d',3)
obj.add_edge('b','e',15)
obj.add_edge('d','e',8)
obj.display()
obj.dijikstra('a','e')
print(obj.bfs('a'))
print(obj.dfs('a'))