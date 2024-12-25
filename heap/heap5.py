class Minheap:
    def __init__(self):
        self.heap = []

    def insert(self,data):
        self.heap.append(i)
        self.heapify_up(len(self.heap)-1)
    
    def heapify_up(self,n):
        parent = (n-1)//2
        if n>0 and self.heap[n] < self.heap [parent]:
            temp = self.heap[n]
            self.heap[n] = self.heap[parent]
            self.heap[parent] = temp
            self.heapify_up(parent)

    def delete(self):
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0,len(len(self.heap)))
        return root

    def heapify_down(self,index,size):
        left = 2*index+1
        right = 2*index+2
        smallest = index
        if left<size and self.heap[left] <self.heap[smallest]:
            smallest = left
        if right<size and self.heap[right]<self.heap[smallest]:
            smallest = right
        if smallest!= index :
            self.heap[smallest],self.heap[index] = self.heap[index],self.heap[smallest]
            self.heapify_down(smallest,size) 

    def getheap(self):
        print(self.heap)

    def heap_sort(self):
        n = len(self.heap)
        for i in range(n//2-1,-1,-1):
            self.heapify_down(i,n)
        # print(self.heap,'dfs')
        for i in range(n - 1, -1, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heapify_down(0,i)
        self.heap.reverse()


obj = Minheap()
lst = [10,2,5,8,6,9,4]
for i in lst:
    obj.insert(i)

obj.getheap()
# obj.delete()
obj.getheap()
obj.heap_sort()
obj.getheap()