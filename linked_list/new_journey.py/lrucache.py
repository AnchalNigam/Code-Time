

class ListNode:
    def __init__(self, data):
        self.val = (data, 0)
        self.next = None
class Cache():
    def __init__(self):
        self.head = None
    def insert(self, key, counter):
        curr = self.head
        prev = None
        node = ListNode(key)
        if curr is None:
            self.head = node
        while curr:
            if curr.val[1] > counter:
                prev = curr
                curr = curr.next
            else:
                if prev is None:              
                    node.next = self.head
                    self.head = node
                
                else:
                    next = prev.next
                    prev.next = node
                    node.next = next
                curr = None
    def update(self, key, counter):
        curr = self.head
        prev = None
        print(curr.val, key,'check')
        while curr:
            if curr.val[0] != key:
                print('yes', key)
                prev = curr
                curr = curr.next
            else:
                if prev is not None:
                    next = curr.next
                    prev.next = next                    
                else:
                    print(self.head, 'next')
                    # temp = self.head
                    self.head = self.head.next
                curr = None
                    # temp = None                  
        self.insert(key, counter)
      
    def remove(self):
        curr = self.head
        prev = None
        while curr and curr.next:
            prev = curr
            curr = curr.next

        if prev is None:
            self.head = None
        else:
            prev.next = None
            
        return curr.val    
        
        
    
def findCacheValue(arr, m, n):
    result = []
    capacity = 0
    cache = Cache()
    dic = {}
    for case in arr:
        if case[0] == 1:
            print(capacity, n)
            if capacity == n:
                removedVal = cache.remove()
                print(removedVal, 'yesff')
                del dic[removedVal[0]]
            if case[1] in dic:
                dic[case[1]][0] = case[2]
                print(dic, case[1], 'dic')
            else:
                dic[case[1]] = [case[2], 0]
                capacity += 1
                cache.insert(case[1], 0)
                    
        else:
            if case[1] not in dic:
                result.append(-1)
            else:
              
                result.append(dic[case[1]][0])
                counter = dic[case[1]][1]+1
                cache.update(case[1], counter)
            
    return result
    
print(findCacheValue([
[1, 1, 1],
[1, 3, 91],
[2, 1]
], 3, 1))

# this is questn of code studio where least recently used we dont just to remove
# we need to maintain how many times it gets accessed and if accessibility count is
# same for two keys then least one remove so here quest has two problem statements
# frst to maintain count and second maintain count in such a way that least recently used should be
# at last...so i used dict and single linked list as i cant make better use of doubly linked
# list...because we have to search counter and then insert after that so traversing toh hai
# so yahn main thought hai dic me value and counter save kro ..and linkedlist me
# key and counter and insertion me check whether cache is full or not if full
# then delete last one and also del from dic and update capacity...if cache is empty and
# value is there just update its value as linkedlist me need nhi hai whi j dusra wala lru 
# leetcod ka questn hai there i have removed that node from ll and append it at frst because
# whn insertion me frst pe hna chahye and manfunda least used ka h yahn counter k h toh ll me na badla
# just dic me badla and if wo nhi h dic me toh counter k jagah find kia and whn pe
# insert kr dia
# if get ops hai toh uska value dic se dia bt uska counter badha ke jahan tha whn delete krke
# proper counter wale jagah pe lagaya so this way handled lru
# time complexity as we seach for counter toh worst case me o(n)
# space is o(n) as each node ka val, next use h rha hai and for n nodes
# n is cache length..get ops ka o(n), put ka bhi o(n)+(n) [rremove+insert] so indrctly o(n)
