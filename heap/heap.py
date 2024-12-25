class Minheap :
    def __init__(self):
        self.heap =[]
    
    def parent(self, i):
        return (i - 1) // 2
    
    def insert(self, key):
        """Insert a new key into the heap."""
        self.heap.append(key)
        i = len(self.heap) - 1
        # Fix the min heap property if it is violated
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
    def min_heapify(self, i):
        """Ensure the heap property is maintained starting from index i."""
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def extract_min(self):
        """Remove and return the minimum element from the heap."""
        if len(self.heap) == 0:
            return None

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.min_heapify(0)

        return root

    def peek_min(self):
        """Return the minimum element without removing it."""
        if len(self.heap) == 0:
            return None
        return self.heap[0]
   
    def get_heap(self):
        """Return the heap."""
        return self.heap
    
obj = Minheap()
lst = [10,20,5,6,2,8]
for i in lst:
    obj.insert(i)

print(obj.get_heap())
print(obj.extract_min())
print(obj.extract_min())
print(obj.peek_min())