
class Stack:
    def __init__(self):
        self.stack = []
        self.stack2 = []
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        if self.stack:

            return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    
    def display(self):
        
        print(self.stack)

    def is_empty(self):
        return len(self.stack)==0
    
    def queue(self):
        while self.stack:
            self.stack2.append(self.stack.pop())
        
        self.stack = self.stack2
        print(self.stack)

    def reverse(self):
        if not self.stack:
            return
        top = self.stack.pop()
        self.reverse()
        self.insert(top)

    def insert(self,data):
        if not self.stack or data > self.stack[-1]:
            self.stack.append(data)
        else:
            top = self.pop()
            self.insert(data)
            self.stack.append(top)
        
    def sort(self):
        while self.stack:
            current = self.stack.pop() 

            while self.stack2 and self.stack2[-1] > current:
                self.stack.append(self.stack2.pop())

            self.stack2.append(current)

        return self.stack2




obj = Stack()
lst = [3,19,6,9,7,1]
for i in lst :
    obj.push(i)

print(obj.pop())
print(obj.peek())
obj.display()
# print(obj.is_empty())
# obj.queue()
# obj.reverse()
obj.display()
print(obj.sort())
# print(obj.peek())