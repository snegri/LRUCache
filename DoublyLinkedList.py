class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def getHead(self):
        return self.head

    def getTail(self):
        if self.tail != None:
            return self.tail

    def show(self):
        temp = self.head
        while temp != None:
            print str(temp.val) + " <->",
            temp = temp.next
        print '\n'

    def append(self, node):
        if self.head == None:
            self.head = node
            node.next = None
            node.prev = None
            #self.tail = node
        elif self.tail == None:
            self.tail = node
            node.prev = self.head
            self.next = None
            self.head.next = self.tail
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def retrieve(self, node):
        if node == self.head:
            if node.next == self.tail:
                node.next.prev = None
                self.tail.next = node
                node.prev = self.tail
                self.head = self.tail
                self.tail = node
                self.tail.next = None
                self.head.prev = None
            else:
                self.head = node.next
                self.head.prev = None
                node.next.prev = None
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                self.tail.next = None
        elif node == self.tail:
            return
        else:
            print node.prev.val
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            self.tail = node
            self.tail.next = None

    def evict(self, node):
        print "Evicted key, value: " + str(node.key) + " " + str(node.val)
        self.head.next.prev = None
        self.head = self.head.next
        del node



class Node(object):
    def __init__(self):
        self.next = None
        self.prev = None
        self.key = None
        self.val = None
