class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        self.stack.pop()
    
    def display(self):
        for i in reversed(self.stack):
            print(i)

    def sort(self):
        temp = []
        while self.stack:
            current = self.stack.pop()
            while temp and temp[-1]>current:
                self.stack.append(temp.pop())
            temp.append(current)
        return temp

    def is_empty(self):
        return len(self.stack) == 0


    
obj = Stack()
obj.push(6)
obj.push(2)
obj.push(2)
obj.push(7)

obj.display()
# obj.pop()
print('fg')
# obj.display()
print(obj.sort())