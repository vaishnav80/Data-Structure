class Node:

    def __init__(s,data):
        s.data = data
        s.next = None
    
class linked:
    def __init__(s):
        s.head = None
    
    def append(s,data):

        new = Node(data)
        if not s.head:
            s.head = new
        else:
            current = s.head
            while current.next:
                current = current.next
            current.next = new

    def display(s):
        current = s.head
        while current:
            print(current.data)
            current = current.next
        
lst = [85,4,2,6,5,2,5,35]
l = linked()
for i in lst:
    l.append(i)
l.display()