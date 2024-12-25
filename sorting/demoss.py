class Queue:

    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = -1

    def enqueue(self,data):
        self.queue.append(data)
        self.rear+=1
    
    def dequeue(self):
        print(self.queue[self.front],'dequed')
        self.front +=1

    def display(self):
        j=self.front
        for i in range(j,len(self.queue)):
            print(self.queue[j])
            j+=1

obj = Queue()
obj.enqueue(6)
obj.enqueue(3)
obj.enqueue(4)
obj.dequeue()
obj.display()