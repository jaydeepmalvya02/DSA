class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertAtFirst(self, data):
        n = Node(data)
        if self.head is None:
            self.tail = n
        n.next = self.head
        self.head = n
        self.tail.next = n

    def InsertAtLast(self,data):
        n=Node(data,self.tail.next)
        self.tail.next=n
        self.tail=n

    def Search(self,value):
        if self.head is not None:
            if self.head.item==value:
                return self.head
            else:
                temp=self.head.next
                while temp.item!=value:
                    temp= temp.next
                return temp

    def InsertAfter(self,target,data):
        n=Node(data,target.next)
        target.next=n

    def ViewList(self):
        if self.head is None:
            print("Empty")
        else:
            print(self.head.item,end="->")
            temp=self.head.next
            while temp !=self.head:
                print(temp.item,end="->")
                temp=temp.next

    def DeletefromFirst(self):
        if self.head is not None:
            if self.head==self.tail:
                self.head=None
                self.tail=None
            self.head = self.head.next
            self.tail.next=self.head

    def DeletefromLast(self):
        if self.head is not None:
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                temp=self.head.next
                while temp.next !=self.tail:
                    temp=temp.next
                temp.next=self.head
                self.tail=temp

    def DeleteNode(self,value):
        if self.head is not None:
            if self.head==self.tail and self.head.item==value:
                self.head=None
                self.tail=None
            elif self.tail.item==value :
                self.DeletefromLast()
            elif self.head.item==value:
                self.DeletefromFirst()
            else:
                temp=self.head.next
                while temp.next.item!=value:
                    temp=temp.next
                temp.next=temp.next.next







c = CLL()
c.InsertAtFirst(30)
c.InsertAtFirst(20)
c.InsertAtFirst(10)

c.InsertAtLast(40)
c.InsertAfter(c.Search(30),35)

c.DeleteNode(35)
c.ViewList()