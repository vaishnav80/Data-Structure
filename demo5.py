class Minheap:
    def __init__(self):
        self.heap = []

    def insert(self,data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)
    

    def heapify_up(self,n):
        parent = (n-1)//2
        if n>0 and  self.heap[n] < self.heap[parent]:
            self.heap[parent],self.heap[n] = self.heap[n],self.heap[parent]
            self.heapify_up(parent)
        
    def display(self):
        print(self.heap)
    
obj = Minheap()
lst = [2,1,4,5,6,1]
for i in lst:
    obj.insert(i)
obj.display()