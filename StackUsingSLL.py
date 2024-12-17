class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Stack:
    def __init__(self):
        self.start=None
        self.count=0
    def IsEmpty(self):
        return self.start==None

    def Push(self,data):
        n=Node(data,self.start)

        self.start=n
        self.count+=1


    def Pop(self):
        if self.start is not None:
            x= x = self.start.item
            if self.start.next is None:

                self.start=None

            else:

               self.start=self.start.next
            self.count-=1
            return x

    def Size(self):
        return self.count

    def Peek(self):
        return self.start.item

s=Stack()
s.Push(10)
s.Push(20)
s.Push(30)
print(s.Pop())
print(s.Peek())
print(s.Size())


