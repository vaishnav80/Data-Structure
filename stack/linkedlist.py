class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack :
    def __init__(self):
        self.head = None
    
    def push(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new
        
    def disaplay(self):
        pass

    def pop(self):
        a = self.head
        self.head = self.head.next
       
        return a.data
        

    def peek(self):
        print(self.head.data)


obj = Stack()
obj.push(6)
obj.push(8)
print(obj.pop())
obj.peek()
obj.disaplay()