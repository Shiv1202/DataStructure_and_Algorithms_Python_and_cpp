class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = dict()
        self.tail = ListNode('t')
        self.head = ListNode('h')
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        cur = self.d[key][1]
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        cur.next = self.head.next
        cur.prev = self.head
        cur.next.prev = cur
        self.head.next = cur
        return self.d[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = (value,self.d[key][1])
            self.get(key)
            return
        
        cur = self.head.next
        cur.prev = ListNode(key)
        cur.prev.next = cur
        cur.prev.prev = self.head
        self.head.next = cur.prev            
        if not self.cap:
            cur = self.tail.prev
            del self.d[cur.val]
            cur.prev.next = self.tail
            self.tail.prev = cur.prev
        else:
            self.cap -=1 
        self.d[key] = (value,self.head.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
