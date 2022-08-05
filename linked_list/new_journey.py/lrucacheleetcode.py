class CacheNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.head = CacheNode(0,0)
        self.n = capacity
        self.capacity = 0
        self.dic = {}
        self.tail = CacheNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def removeFromTail(self):
        prevv = self.tail.prev
        self.removeFromList(prevv)
        return prevv.key
    def removeFromList(self, node):
        prevv = node.prev
        nextt = node.next
        prevv.next = nextt
        nextt.prev = prevv
        
            
    def insertAtHead(self, node):
        nextt = self.head.next
        self.head.next = node
        node.next = nextt
        node.prev = self.head
        nextt.prev = node
        
        
        
        

    def get(self, key: int) -> int:
      
        
        if key in self.dic:      
            # print('inside')
            node = self.dic[key]
            self.removeFromList(node)
            self.insertAtHead(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        node = CacheNode(key, value) 
        # print(self.dic, 'p')
        if key in self.dic: 
            node2 = self.dic[key]
            self.removeFromList(node2)
        else:            
            if self.capacity == self.n:
                removedNode = self.removeFromTail()
                # print(node, 'yes')
                # print(removedVal, 'chec')
                del self.dic[removedNode]
                self.capacity -= 1       
            self.capacity += 1
        self.insertAtHead(node)         
        self.dic[key] = node
        # print(self.dic, 'dic', key)
       
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# here doubly linkedlist ka use hua hai and dict ka...so o(n) space keh lo and o(1) for get
# put ops
# scene yahn doubly ka sekha kki just have tail as well and dummy head and tail lia
# so that to avoid if sel.fhead is none and all....code readaility is better by having dummy
# tail and head...just to add node at front take next of dummy node and attach node.next
# to nextt and prev to self.head [look insertathead funct] so this way insertion h rha hai
# if it exists in dic then remove it from list, removing is quite easy..just get that node
# and node ka prev next tod do...so dic me node k rkhne k sense ye h hai ki directly node 
# se delete ops h islie self.val bhi rkha hai so that every info us key k against rhe , its value
# so this way handle hua h...loook at code..easy hai