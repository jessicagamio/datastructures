class LinkedList(object):
    """creates Linked list"""
    def __init__(self):
        self.head=None
        self.tail=None

    def appendNode(self,node):
        """Adds node to list"""
        if self.head == None:
            self.head=node
        if self.tail != None:
            self.tail.next=node
        self.tail=node

    def removeNode(self, data):
        """removes  item from linked list"""
        if self.head.data == data: 
            self.head = self.head.next

        curr = self.head
        prev = None
        found = False

        while not found:
            if curr.data == data:
                print('We found berry')
                found = True
            else:
                prev = curr
                curr = curr.next

        if prev == None:
            self.head = curr.next

        else:
            prev.next=curr.next


class Node(object):
    """create node"""
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

    def addNode(self, data):
        """adds node"""
        node=Node(data)

        if self.next == None:
            self.next = node

        else:
            while self.next != None:
                self = self.next

            self.next = node


mynode=Node('apple',Node('berry',Node('cheery')))

mylist=LinkedList()

curr = mynode

while curr != None:
    mylist.appendNode(curr)
    curr = curr.next

print('head ==>', mylist.head.data)
print('tail ==>', mylist.tail.data)

mylist.removeNode('berry')

print('head.next ==>', mylist.head.next.data)