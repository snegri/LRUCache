import DoublyLinkedList


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.currCap = 0
        self.store = {}
        self.linkedList = DoublyLinkedList.DoublyLinkedList()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #self.linkedList.retru

        temp = self.store.get(key, None)
        #print temp.key
        if temp == None:
        	print "-1"
        	return
        self.linkedList.retrieve(temp)
        #print "Got " + str(temp.val) + " successfully."
        #print "-----------------------"
        #self.linkedList.show()
        #print "-----------------------"

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.currCap >= self.cap:
        	head = self.linkedList.getHead()
        	print head.key
        	self.linkedList.evict(head)
        	self.store[head.key] = None
        	del self.store[head.key]
        insert = DoublyLinkedList.Node()
        insert.val = value
        insert.key = key
        self.store[key] = insert
        #print "-----------------------"
        self.linkedList.append(insert)
        #self.linkedList.show()
        #print "-----------------------"
        self.currCap += 1




cache = LRUCache(2);

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       #// returns 1
cache.put(3, 3);    #// evicts key 2
cache.get(2);       #// returns -1 (not found)
cache.put(4, 4);    #// evicts key 1
cache.get(1);       #// returns -1 (not found)
cache.get(3);       #// returns 3
cache.get(4);       #// returns 4