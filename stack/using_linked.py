class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            print("underflow")
        print(self.head.data,'poped data')
        self.head = self.head.next

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    
obj = stack()
obj.push(5)
obj.push(9)
obj.push(4)
obj.pop()
obj.display()