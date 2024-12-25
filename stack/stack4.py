class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def display(self):
        for i in reversed(self.stack):
            print(i,end="")

    def recursion(self):
        if not self.stack:
            return 0
        
        n = self.stack.pop()
        self.recursion()
        self.insert(n)

    def insert(self,n):
        if not self.stack:
            self.stack.append(n)
        else:
            top = self.stack.pop()
            self.insert(n)
            self.stack.append(top)
        
    def sort(self):
        if not self.stack:
            return 0
        
        n = self.stack.pop()
        self.sort()
        self.insert(n)
    
    def insert(self,n):
        if not self.stack or n>self.stack[-1]:
            self.stack.append(n)
        else:
            top = self.stack.pop()
            self.insert(n)
            self.stack.append(top)


lst = [4,8,6,5,3,2]
obj = Stack()
for i in lst:
    obj.push(i)
obj.pop()
print(obj.peek())
obj.display()
obj.recursion()
print()
obj.sort()
obj.display()