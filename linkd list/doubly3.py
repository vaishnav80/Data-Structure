class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class doub:

    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
        else:

            current = self.head
            while current.next:
                current = current.next
            
            a = Node(data)
            current.next = a
            a.prev = current
    
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def reverse(self):
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

obj = doub()
obj.insert(6)
obj.insert(9)
obj.insert(8)
obj.display()