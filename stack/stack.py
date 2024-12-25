class Stack:

    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
    
    def display(self):
        print(self.stack)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None
     
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def sort(self):
        temp = []
        while self.stack:
            current = self.stack.pop()
            while temp and temp[-1]>current:
                self.stack.append(temp.pop())
            temp.append(current)
        return temp

obj = Stack()
lst = [3,6,4,3,2,6]
for i in lst:
    obj.push(i)

obj.display()
print(obj.pop())
obj.display()
print(obj.is_empty())
print(obj.peek())
obj.display()
print('sorted array',obj.sort())
