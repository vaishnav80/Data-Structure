class Heap:
    def __init__(self):
        self.heap = []
    
    def insert(self,data):
        
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)
    
    def heapify_up(self,n):
        parent = (n-1)//2
        if n>0 and self.heap[n] > self.heap[parent]:
            self.heap[parent],self.heap[n] = self.heap[n],self.heap[parent]
            self.heapify_up(parent)

    def extract(self):
        temp = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return temp
    
    def heapify_down(self,n):
        left = 2*n+1
        right = 2*n+2
        largest = n

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left  
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right       

        if largest != n:
            self.heap[largest],self.heap[n] = self.heap[n],self.heap[largest]
            self.heapify_down(largest)
    def display(self):
        print(self.heap)

    def sort(self):
        n = len(self.heap)
        for i in range(n-1,-1,-1):
            self.heap[0],self.heap[i] = self.heap[i],self.heap[0]
            self.heapifydown(0,i)
    
    def heapifydown(self,i,n):
        
        left = 2*i+1
        right = 2*i+2
        largest = i

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left

        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]
            self.heapifydown(largest,n)
        

obj = Heap()
lst = [3,4,6,5,9,7,2,19,16,13]
for i in lst:
    obj.insert(i)
obj.display()
# print(obj.extract())
# obj.display()
obj.sort()
obj.display()