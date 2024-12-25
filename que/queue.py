class Queue:

    def __init__(self):
        self.queue=[]
        self.front= 0
        self.rear = -1

    def enqueue(self,data):
        self.queue.append(data)
        self.rear +=1

    def dequeue(self):
        if self.isempty():
            print("queue is empty")
        print(self.queue[self.front])
        self.front+=1

    def peek(self):
        if self.isempty():
            print("queue is empty")
        print(self.queue[self.front],'f')

    def isempty(self):
        return self.front  > self.rear


obj = Queue()
obj.enqueue(5)
obj.enqueue(6)
obj.enqueue(9)
obj.peek()
obj.dequeue()
obj.peek()
