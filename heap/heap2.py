class Minheap:
    def __init__(self):
        self.heap = []

    def insert(self,key):
        self.heap.append(key)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self,index):
        parent = (index-1)//2
        if index>0 and self.heap[index]<self.heap[parent]:
            temp = self.heap[index]       
            self.heap[index]  = self.heap[parent]
            self.heap[parent] = temp
            self.heapify_up(parent)    

    def delete(self):
        if len(self.heap)==0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return root
    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        print(right,'right')
        print(len(self.heap),'cxcv') 
        smallest = index
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    def peek(self):
        print(self.heap[0])

    def getheap(self):
        print(self.heap)

    def heap_sort(self):
        n = len(self.heap)-1
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)

        for i in range(n - 1, -1, -1):
            print(i)
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heapify_down(0) 
       

obj = Minheap()
lst = [10,2,5,8,6,9,2]
for i in lst:
    obj.insert(i)

# obj.getheap()
# # obj.delete()
# obj.getheap()
# obj.heap_sort()
obj.getheap()
