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
        if self.head==node: 
            self.head = self.head.next

        curr = self.head
        prev = None
        found = False

        while not found:
            if curr.data == node.data:
                found = True
            
            prev = curr
            curr = curr.next

        if prev == None:
            self.head = curr.next

        else:
            prev.next=curr.next


class Node(object):
    """create node"""
    def __init__(self, data):
        self.data=data
        self.next=None

    def addNode(self, data):
        """adds node"""
        node = Node(data)

        if self.next == None:
            self.next = node

        self.next.next = node


