# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             last = self.head
#             while last.next:
#                 last = last.next
#             last.next = new_node
        
#     def reverse(self):
#         current = self.head
#         prev = None
#         new = None

#         while current:
#             new = current.next
#             current.next = prev
#             prev = current
#             current = new
            
#         self.head = prev
    
    
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next
    


# l = Linkedlist()
# lst = [2,12,14,56,6,7,46]
# for i in lst:
#     l.append(i)
# l.reverse()
# l.display()



class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class linked:
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

    def display(self):
        current = self.head
        count = 0

        while current:
            print(current.data,count)
            count+=1
            current = current.next

    def reverse(self):
        current = self.head
        prev = None
        next = None
        while current:
            next = current.next
            current.next = prev
            prev =current
            current = next
        
        self.head = prev


obj = linked()
lst = [4,5,6,2]
for i in lst:
    obj.append(i)
obj.reverse()
obj.display()