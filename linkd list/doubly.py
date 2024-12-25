class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None 
        self.next = None

class doubly:
    def __init__(self):
        self.head = None

    def append(self,data):
        new = Node(data)
        if not self.head :
            self.head = new
            return 
        current = self.head
        while current.next:
             
            current = current.next
        current.next = new
        new.prev = current

    def appendfirst(self,data):
        new = Node(data)
        if not self.head :
            self.head = new
            return 
        current = self.head
        current.prev = new
        self.head = new
        new.next = current
        new.prev = None

    def insert(self,data,new):
        new = Node(new)
        if not self.head:
            self.head = new
        current = self.head
        while current and current.data!=data:
            current = current.next

        if not current:
            print(f"Node with data {data} not found.")
            return
        a = current.next
        new.prev = current
        current.next = new
        new.next = a

    def before(self,data,new):
        new = Node(new)
        if not self.head:
            self.head = new
        current = self.head
        while current and current.data!=data:
            prev = current
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next


obj = doubly()

obj.append(5)
obj.append(6)
obj.append(9)
obj.insert(9,15)
obj.appendfirst(14)
obj.display()
        