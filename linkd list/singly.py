class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        print(new_node,'jhj')
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def inserted_first(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new
        
    def inserted_last(self,data):
        new = Node(data)
        if not self.head:
            self.head = new
        last = self.head
        while last.next:
            last = last.next
        last.next = new
    
    def delete_node(self,data):
        if not self.head:
            print('the list is empty')
        if self.head.data == data:
            self.head = self.head.next
            return 
        else:
            current = self.head
            prev = None
            while current and current.data != data:
                prev = current
                current = current.next
            if not current:
                print('not found')

            prev.next = current.next

    def insert(self,data,n):
        if not self.head:
            print('the list is empty')
        current = self.head
        # print(current.data)
        # print(data)
        while current and current.data!=data:
            current = current.next

        new = current.next   
        new_node = Node(n)
        current.next = new_node
        new_node.next = new     

    def prev_insert(self,data,n):
        if not self.head:
            print('the list is empty')
        
        current = self.head
        while current and current.data!=data:
            prev = current
            current = current.next
     
        new_node = Node(n)
        prev.next = new_node
        new_node.next = current


    def delete_after(self,data):
        if not self.head:
            print('the list is empty')
            return
        current = self.head
        while current and current.data != data:
            current = current.next
        print(current.next)
        current.next = current.next.next
    
    def delete_before(self,data):
        if not self.head or  self.head.data == data:
            print('the list is to short')
            return
        current = self.head
        prev = None
        before_prev = None
        while current and current.data != data:
            before_prev = prev
            prev = current
            current = current.next
        if prev == self.head:
            self.head = self.head.next
        else:
            before_prev.next = current

    def duplicates(self):
        if self.head is None :
            return None
        current = self.head
        prev = None
        seen = set()
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

        return 
    def duplicates_count(self):
        if self.head is None :
            return None
        current = self.head
        
        count = {}
        while current:
            if current.data in count:
                count[current.data] +=1 
            else:
                count[current.data] =1 
            current = current.next
            

        for key, count in count.items():
            if count > 1:
                print(key, end=" ")
        
        print()
    
l = Linkedlist()
lst = [2,12,14,56]
for i in lst:
    l.append(i)
l.append(5)
l.append(5)
l.append(6)
# l.inserted_first(9)
# l.inserted_last(1)
# l.display()
# l.duplicates()
# l.delete_node(6)
# l.insert(1,10)
# l.delete_before(5)
# l.prev_insert(1,3)
# l.display()
# l.duplicates_count()
