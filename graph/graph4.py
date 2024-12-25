import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}
    
    def add_edge(self,v1,v2,a,b):
        if v1 not in self.graph:
            self.graph[v1] = {}
        if v2 not in self.graph:
            self.graph[v2] = {}
      
        self.graph[v1][v2]=a
        self.graph[v2][v1]=b
            
        
    def remove_edge(self,v1,v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)
            

    def remove_vertex(self,v1):
        if v1 in self.graph:
            for i in self.graph:
                if v1 in self.graph[i]:
                    self.graph[i].remove(v1)

    def has_edge(self,v1,v2):
        if v1 in self.graph and v2 in self.graph:
            if v1 in self.graph[v2] and v2 in self.graph[v1]:
                return True
            else:
                return False
        else: 
            return False
    def display(self):
        for k,v in self.graph.items():
            print(k,v)

    def bfs(self,v1):
        if v1 in self.graph:
            queue = [v1]
            visited = [v1]
            while queue:
                cur = queue.pop(0)
                for i in self.graph[cur]:
                    if i not in visited:
                        visited.append(i)
                        queue.append(i)
            return visited
        
    def dfs(self,v1,visited = None):
        if v1 in self.graph:
            if visited is None:
                visited = []
            visited.append(v1)
            for i in self.graph[v1]:
                if i not in visited:
                    self.dfs(i,visited)
               
            return visited
        
    def dijkstra(self, start):
        # Min-heap priority queue to store (distance, vertex)
        queue = [(0, start)]
        # Dictionary to store the shortest distance from start to each vertex
        distances = {vertex: float('inf') for vertex in self.graph}
        # Set distance to the start node to 0
        distances[start] = 0
        # Dictionary to store the previous node (for path reconstruction)
        previous = {vertex: None for vertex in self.graph}

        while queue:
            # Get the vertex with the smallest distance
            current_distance, current_vertex = heapq.heappop(queue)

            # Loop through neighboring nodes of the current vertex
            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_distance + weight

                # Only consider this new path if it's shorter than the previous path
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(queue, (distance, neighbor))

        return distances, previous

    # Function to get the shortest path from start to a target vertex
    def get_shortest_path(self, previous, target):
        path = []
        current = target
        while current is not None:
            path.insert(0, current)
            current = previous[current]
        return path
    
    def dijkstras(self, start, target):
        queue = [(0, start)]  # (distance, vertex)
        distances = {vertex: None for vertex in self.graph}
        distances[start] = 0
        previous = {vertex: None for vertex in self.graph}

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            print(current_vertex)
            

            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_distance + weight
                print(distances[neighbor])
                if distances[neighbor] is None or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(queue, (distance, neighbor))

        # Reconstruct path
        path = []
        current = target
        print(previous)
        while current is not None:
            path.insert(0, current)
            current = previous[current]

        return path, distances[target],distances
    



obj = Graph()
obj.add('q')
obj.add('b')
obj.add('a')
obj.add_edge('a','q',5,6)
obj.add_edge('a','c',3,8)
obj.add_edge('b','q',7,4)
obj.add_edge('b','c',2,5)
# print(obj.has_edge('b','a'))
# obj.remove_edge('b','q')
# obj.display()
# print(obj.bfs('q'))
# print(obj.dfs('q'))

print(obj.dijkstras('q','c'))
# print(obj.get_shortest_path('q','c'))