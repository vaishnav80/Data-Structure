class Node:
    def __init__(self,data):
        self.data = data
        self.next= None

    
class Linked:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        new = Node(data)
        if not self.head:
            self.head = new
        
        else :
            last = self.head
            while last.next:
                last = last.next
            last.next = new
        
    
    def display(self):
        current = self.head
        while current:
            print(current.data,end=" ")
            current = current.next

    def reverse(self):
        current =self.head
        prev = None
        temp = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def middle(self):
        current = self.head
        slow = current
        fast = current
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data,'ds')

    def insertat(self,n,data):
        current = self.head
        prev = self.head
        count = 1
        while current and count!=n:
            prev = current
            current =current.next
            count+=1
        a =  Node(data)
        prev.next = a
        a.next = current

obj = Linked()
obj.insert(6)
obj.insert(8)
obj.insert(10)
obj.insert(12)
obj.insert(14)
obj.display()
# obj.reverse()
# obj.middle()
obj.insertat(3,9)
obj.display()