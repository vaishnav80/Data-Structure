class Graph:
    def __init__(self):
        self.graph= {}
        
    def add(self,v1):
        if v1 not in self.graph:
            self.graph[v1] = {}
        
    def add_edge(self,v1,v2,a):
        if v1 not in self.graph:
            self.graph[v1] = {}
        if v2 not in self.graph:
            self.graph[v2] = {}
        self.graph[v1][v2] = a

    def remove_edge(self,v1,v2):
        if v1 and v2 in self.graph:
            self.graph[v1].remove(v2)
    
    def remove_Vertex(self,v1):
        if v1 in self.graph:
            for i in self.graph:
                if v1 in self.graph[i]:
                    self.graph[i].remove(v1)
            del self.graph[v1]

    def dfs(self,v1,visited = None):
        if visited is None:
            visited = []
        visited.append(v1)
        for i in self.graph[v1]:
            if i not in visited:

                self.dfs(i,visited)
        return visited

    def bfs(self,v1):
        visited = [v1]
        queue = [v1]
        while queue:
            cur = queue.pop(0)
            for i in self.graph[cur]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
        
        return visited
    
    def dijkstras(self,start,end):
        
        queue = [(0,start)]
        distances = {vertex : float('inf') for vertex in self.graph}
        distances[start] = 0
        previous = {vertex : None for vertex in self.graph}
        while queue:
            cur_distance , cur_vertex = queue.pop(0)
            if cur_vertex == end:
                break
            for k,v in self.graph[cur_vertex].items():
                distance = cur_distance + v
                if distance< distances[k]:
                    print(k,v)
                    distances[k] = distance
                    previous[k] = cur_vertex
                    queue.append((distance,k))
        path = []
        cur = end
        while cur:
            path.insert(0,cur)
            cur = previous[cur]
        return path,distances[end]

    def display(self):
        print(self.graph)
    
obj = Graph()
obj.add(6)
obj.add(2)
obj.add(5)
obj.add_edge(5,2,4)
obj.add_edge(6,5,5)
obj.add_edge(6,3,6)
obj.add_edge(7,3,8)
obj.add_edge(3,7,2)
# obj.remove_edge(5,2)
# obj.remove_Vertex(7)
obj.display()
print(obj.dfs(6))
print(obj.bfs(6))
print(obj.dijkstras(6,2))