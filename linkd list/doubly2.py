# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class doubly:
#     def __init__(self):
#         self.head = None
    
#     def append(self,data):
#         new = Node(data)
#         if not self.head:
#             self.head = new
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new
#         new.prev = current

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data,end=" <->" if current.next else " ")
#             current = current.next
        
# l = doubly()
# lst = [2,12,14,56]
# for i in lst:
#     l.append(i)
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
            current =current.next
        
        current.next  = new
    
    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
    
    def display(self):

        current = self.head
        while current:
            print(current.data)
            current = current.next
        

    def remove(self):
        current = self.head 
        lst = set()
        prev = None
        while current:
            if current.data in lst:
                prev.next = current.next
            else:
                prev = current
                lst.add(current.data)
            current = current.next
        return 


lst = [4,5,6,2,6,2,7]
l = linked()
for i in lst:
    l.append(i)
# l.middle()
l.remove()
l.display()


# class Node:

#     def __init__(self,data):
#         self.data = data
#         self.next= None
#         self.prev = None


# class double:

#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new = Node(data)

#         if not self.head:
#             self.head = new
#             return
        
#         current = self.head

#         while current.next:
#             current = current.next
        
#         current.next = new
#         new.prev = current

#     def display(self):
#             current = self.head
#             while current:
#                 print(current.data, end=" <-> " if current.next else "")
#                 current = current.next

#     def middle(self):
#         slow = self.head
#         fast = self.head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         prev = slow.prev
#         next = slow.next
#         prev.next = next
#         next.prev = slow
#         return slow.data


# obj = double()

# obj.append(5)
# obj.append(6)
# obj.append(9)
# # obj.insert(9,15)
# # obj.appendfirst(14)

# obj.middle()
# obj.display()