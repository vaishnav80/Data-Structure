# lst = [1,3,5,7,9]

# def sum(lst,i=0):
#     if i==len(lst):
#         return 1
#     return lst[i]+sum(lst,i+1)
    
# print(sum(lst))


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
        while current:
            print(current.data,end=" ")
            current = current.next
        
    def middle(self):
        min = self.head
        max = self.head
        current = self.head
        prev = None
        while current.next and max.next:
            
            prev = current
            min = current.next
            max = current.next.next
            current = current.next
            
        return min.data

obj = linked()
lst = [2,5,6,7,4]
for i in lst:
    obj.append(i)

obj.display()
print('midle',obj.middle())