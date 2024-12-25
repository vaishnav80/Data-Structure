class Heap:
    def __init__(self):
        self.heap = []
    
    def insert(self,data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self,n):
        parent = (n-1)//2
        if n>0 and self.heap[parent]<self.heap[n]:
            self.heap[parent],self.heap[n] = self.heap[n],self.heap[parent]
            self.heapify_up(parent)

    def extract(self):
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)

    def heapify_down(self,n):
        left = 2*n+1
        right = 2*n+2
        largest = n
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != n:
            self.heap[n],self.heap[largest] = self.heap[largest],self.heap[n]
            self.heapify_down(largest)

    def sort(self):
        n = len(self.heap)
        for i in range(n-1,-1,-1):
            self.heap[0],self.heap[i] = self.heap[i],self.heap[0]
            self.heapify_sort(0,i)
    def heapify_sort(self,index,size):
        left = 2*index+1
        right = 2*index+2
        largest = index
        if left < size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index],self.heap[largest] = self.heap[largest],self.heap[index]
            self.heapify_sort(largest,size)


    def display(self):
        print(self.heap)

obj = Heap()
lst = [6,5,8,8,4,3,5]
for i in lst:
    obj.insert(i)
obj.display()
# obj.extract()
obj.sort()
obj.display()
