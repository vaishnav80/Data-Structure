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
        
    def reverse(self,head):
        current = head
        prev = None
        new = None

        while current:
            new = current.next
            current.next = prev
            prev = current
            current = new
            
        return prev
    
    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True  # Empty or single element list is a palindrome

        # Step 1: Find the middle of the linked list
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        second_half_head = self.reverse(slow)
        
        # Step 3: Compare the first half and the reversed second half
        first_half_head = self.head
        while second_half_head:
            if first_half_head.data != second_half_head.data:
                return False
            first_half_head = first_half_head.next
            second_half_head = second_half_head.next

        return True
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    


l = Linkedlist()
lst = [2,12,14,56,6,7,46]
for i in lst:
    l.append(i)
print(l.is_palindrome())
l.display()