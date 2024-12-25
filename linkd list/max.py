class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        
    def max(self):
        current = self.head
        max = current
        max2 = current
        while current:
            if current.data>max.data:
                max2 = max
                max = current
            elif current.data>max2.data and current.data<max.data:
                max2 = current

            current = current.next
        
        
        return max.data,max2.data


l = Linkedlist()
lst = [2,12,14,56,6,123,7,46]
for i in lst:
    l.append(i)

print(l.max())