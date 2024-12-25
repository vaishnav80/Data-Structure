class Heap:
    def __init__(self):
        self.heap = []

    def insert(self,data):
        self.heap.append(data)
        self._heapify_up(len(self.heap)-1)
    
    def _heapify_up(self,n):
        parent = (n-1) // 2
        if n>0 and self.heap[parent]>self.heap[n]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[n]
            self.heap[n]  = temp
            self._heapify_up(parent)
        
    def display(self):
        print(self.heap)

    def delete(self):
        temp = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return temp
    
    def heapify_down(self,i):
        left = 2*i+1
        right = 2*i+2
        largest = i
        if left<len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right<len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest!=i:
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]
            self.heapify_down(largest)

    def sort(self):
        n = len(self.heap)
        for i in range(n-1,-1,-1):
            self.heap[i],self.heap[0] = self.heap[0],self.heap[i]
            self.heapify(0,i)
        
    def heapify(self,i,n):
        left = 2*i+1
        right = 2*i+2
        largest = i
        if left<n and self.heap[left] < self.heap[largest]:
            largest = left
        if right<n and self.heap[right] < self.heap[largest]:
            largest = right
        
        if largest!=i:
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]
            self.heapify(largest,n)

lst = [10,5,3,2,4,1,25]
obj = Heap()
for i in lst:
    obj.insert(i)

obj.display()
# print(obj.delete())
obj.display()
obj.sort()
obj.display()
