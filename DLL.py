class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next


class DLL:
    def __init__(self):
        self.start = None

    def InsertAtfirst(self, data):
        n = Node(None, data, self.start)
        if not self.start is None:
            self.start.prev = n

        self.start = n

    def InsertAtLast(self, data):
        if self.start is None:
            return self.InsertAtfirst(data)
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n = Node(temp, data)
            temp.next = n

    def ViewList(self):
        if self.start is None:
            print("EMpty")
        else:
            temp = self.start
            while temp is not None:
                print(temp.item, end="<->")
                temp = temp.next

    def InsertAfter(self, target, data):
        n = Node(target, data, target.next)
        if target.next is not None:
            target.next.prev = n

        target.next = n

    def Search(self, value):
        if self.start is not None:
            if self.start.item == value:
                return self.start
            else:
                temp = self.start
                while temp.item != value:
                    temp = temp.next
                return temp

    def DeletefromFirst(self):
        if self.start is not None:
            self.start = self.start.next
            self.start.prev = None

    def DeleteFromLast(self):
        if self.start is not None:
            if self.start.next is None:
                self.start = None
            else:
                temp = self.start
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None

    def DeleteNode(self, value):
        if self.start is not None:
            if self.start.item == value and self.start.next is not None:
                self.start = self.start.next
                self.start.prev = None
            elif self.start.next is None and self.start.item == value:
                self.start = None
            else:
                temp = self.start
                while temp.next != None:
                    if temp.next.next is None and temp.next.item == value:
                        temp.next = None
                    elif temp.next.item == value:
                        temp.next.next.prev = temp
                        temp.next = temp.next.next

                    else:
                        temp = temp.next


d = DLL()
d.InsertAtfirst(30)
d.InsertAtLast(40)

d.InsertAtfirst(20)
d.InsertAtfirst(10)
d.InsertAfter(d.Search(30), 35)
d.DeleteNode(35)
d.ViewList()


