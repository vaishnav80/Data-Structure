# class Stack:

#     def __init__(self):
#         self.stack = []
#         self.stack2 = []

#     def push(self,data):
#         self.stack.append(data)

#     def temp(self):
#         while self.stack:
#             self.stack2.append(self.stack.pop())
#         self.stack = self.stack2
        
#     def reverse(self):
#         if not self.stack:
#             return
#         n = self.stack.pop()
#         self.reverse()
#         self.stack.insert(0,n)
#         print(self.stack,'last')

#     def display(self):
#         for i in reversed(self.stack):
#             print(i)
#         print('ddfsd')
        
# obj = Stack()
# lst = "hello"
# for i in lst:
#     obj.push(i)
# obj.display()
# # obj.temp()
# # obj.display()
# obj.reverse()
# obj.display()


class Stack:
    def __init__(self):
        self.stack = []
        self.stack2 = []
    
    def push(self,data):
        self.stack.append(data)

    def pop(self):
        print(self.stack.pop())
        print(self.stack)

    def insert(self,n):
        if not self.stack or self.stack[-1]<=n:
            self.stack.append(n)
        else:
            top  = self.stack.pop()
            self.insert(n)
            self.stack.append(top)
        print(self.stack)

    def reverse(self):
        if not self.stack:
            return
        n = self.stack.pop()
        self.reverse()
        self.insert(n)

    def reverse_stack(self):
        while self.stack:
            top = self.stack.pop()
            while self.stack2 and self.stack2[-1]>top:
                self.stack.append(self.stack2.pop())
            
            self.stack2.append(top)
        print(self.stack2)

    


obj = Stack()
s = "hello"
for i in s:
    obj.push(i)
obj.pop()
obj.reverse()
obj.reverse_stack()
