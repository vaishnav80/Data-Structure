class Queue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size
        self.front = 0
        self.rear = 0
        

    def enqueue(self,data):
        if not None in self.queue:
            print("queue is full")
        else:   
            self.queue[self.rear] = data
            self.rear = (self.rear+1) % self.size
            

    def dequeue(self):
        if self.queue[self.front] == None:
            print("underflow")
        else:
            print(self.queue[self.front],'de')
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
    
    def peek(self):
        print(self.queue)
    
obj = Queue(6)
obj.enqueue(5)
# obj.enqueue(6)
# obj.enqueue(9)
# obj.enqueue(9)
# obj.enqueue(9)
# obj.enqueue(9)
obj.peek()
obj.dequeue()
obj.dequeue()
# obj.enqueue(2)
# obj.enqueue(20)
# obj.enqueue(2)
# obj.dequeue()
# obj.dequeue()


obj.peek()

        


