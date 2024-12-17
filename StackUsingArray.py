class Stack:
    def __init__(self):
        self.items=[]
        self.count=0
    def Push(self,data):
        self.items.append(data)
        self.count+=1
    def Pop(self):
        x=self.items[-1]
        self.items.pop(-1)
        self.count-=1
        return x
    def Top(self):
        return self.items[-1]

    def Size(self):
        return self.count

s=Stack()
s.Push(50)
s.Push(40)
s.Push(30)
s.Push(20)
s.Push(10)

print(s.Top())
s.Pop()
print(s.items)