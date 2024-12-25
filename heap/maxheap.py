class Maxheap:
    def __init__(self):
        self.heap = []

    
    def insert(self,key):
        self.heap.append(key)
        self._heapify_up(len(self.heap)-1)

    def _heapify_up(self,index):
        parent = (index - 1) // 2
       

        if index > 0 and self.heap[index]>self.heap[parent]:
            
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp

            self._heapify_up(parent)

        
    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def getheap(self):
        return self.heap
    
    def delete(self):
        if len(self.heap)==0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.max_heapify(0)

    def max_heapify(self, i):
        """Ensure the heap property is maintained starting from index i."""
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)


    def heap_sort(self):
        """Perform heap sort on the current heap."""
        n = len(self.heap)

        # Step 1: Build a max heap
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(i)

        # Step 2: Extract elements one by one
        sorted_array = []
        for i in range(n - 1, -1, -1):
            # Move the current root (maximum) to the end
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            sorted_array.append(self.heap.pop())  # Remove the largest element
            self.max_heapify(0)  # Heapify the reduced heap

        # Reverse the sorted_array to get the ascending order result
        return sorted_array[::-1]

obj = Maxheap()
lst = [6,5,4,7,8,2,3]
for i in lst:
    obj.insert(i)

print(obj.getheap())

# print(obj.peek())
# print(obj.heap_sort())
