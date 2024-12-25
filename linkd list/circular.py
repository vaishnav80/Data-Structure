# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class circle:

#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new = Node(data)
#         if not self.head :
#             self.head = new
#             self.head.next = self.head
#             self.head.prev = self.head
#             return
#         a = self.head.prev
#         print(a.data)
#         current = self.head.prev
#         current.next = new
#         new.prev = current
#         new.next = self.head
#         self.head.prev = new
    
#     def display(self):
#         current = self.head
#         while True:
#             print(f"{current.data}", end=" <-> " if current.next != self.head else " -> Head\n")
#             current = current.next
#             if current == self.head:
#                 break 


class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class circle:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new = Node(data)

        if not self.head:
            self.head = new
            new.next = self.head 
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        
        current.next = new
        new.next = self.head
    
    def display(self):

        current = self.head
        while current:
            print(current.data, end=" -> " if current.next != self.head else " -> head")
            current = current.next
            if current == self.head:
                break

lst = [3,5,7,8,23,52,2]

l = circle()
for i in lst:
    l.append(i)
l.display()