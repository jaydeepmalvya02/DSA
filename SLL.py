class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next


class SLL:
    def __init__(self):
        self.start =None

    def InsertAtfirst(self,data):
        n=Node(data,self.start)

        self.start=n
    def InsertAtLast(self,data):
        n=Node(data)
        if self.start is None:
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
    def InsertAfter(self,target,data):
        n=Node(data,target.next)
        target.next=n


    def Search(self,t):
        if not self.start is None:
            if self.start.item==t:
                return self.start
            else:
                temp=self.start
                while temp.item !=t:
                    temp=temp.next
                return temp

    def DeleteFromFirst(self):
        if not self.start is None:
            self.start=self.start.next


    def DeleteFromLast(self):
        if self.start!=None:
            if self.start.next==None:
                self.start=None
            else:
                temp=self.start
                while temp.next.next is not None:
                    temp=temp.next
                temp.next=None
    def ViewList(self):
        if self.start is None:
            print("EMPTY")
        else:
            temp=self.start
            while temp is not None:
                print(temp.item,end="->")
                temp=temp.next

    def DeleteItem(self,t):
        if not self.start is None:

            if self.start.item==t:
                self.start=self.start.next
            else:
                temp=self.start
                while temp.next.item!=t:
                    temp=temp.next
                temp.next=temp.next.next





s=SLL()
s.InsertAtfirst(30)
s.InsertAtfirst(20)
s.InsertAtLast(40)
s.InsertAfter(s.Search(30),35)
s.DeleteItem(35)

s.ViewList()





