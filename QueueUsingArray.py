class Queue:
    def __init__(self):
        self.items=[]
        self.count=0
    def Enqueue(self,data):

        self.items.insert(0,data)
        self.count+=1
    def Dequeue(self):
        x=self.items[-1]
        self.items.pop()
        self.count-=1
        return x

    def GetFront(self):
        return self.items[-1]
    def GetRear(self):
        return self.items[0]
    def Size(self):
        return self.count

q=Queue()
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)
print(q.Dequeue())
print(q.GetRear())
print(q.GetFront())
print(q.items)
