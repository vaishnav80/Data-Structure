class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,data):
        self.stack.append(data)

    def insert(self,element):
        print('called',element)
        if not self.stack or self.stack[-1] <= element:
            self.stack.append(element)
        else:   
            top = self.stack.pop()
            self.insert(element)
            self.stack.append(top)
        
    def sortstack(self):
        if not self.stack:
            return
        top = self.stack.pop()
        self.sortstack()
        self.insert(top)

    def display(self):
        print("Stack from top to bottom:", self.stack)
obj = Stack()
obj.push(6)
obj.push(8)
obj.push(345)
obj.push(90)
obj.push(9)
obj.push(16)
obj.sortstack()
obj.display()