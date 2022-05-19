# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        middleCount = 0
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            middleCount += 1
            fast = fast.next.next
        middleCount += 1
        if fast is None:
            nodesCount = (middleCount-1)*2
        else:
            nodesCount = (middleCount*2)-1
        # print(middleCount, nodesCount)
        nodesNumToDel = (nodesCount-n) + 1
        # print(nodesNumToDel, 'chec')
        if nodesNumToDel > middleCount:
            curr = slow
            prev = None
            while(middleCount < nodesNumToDel):
                prev = curr
                curr = curr.next
                middleCount += 1
            nextt = curr.next
            prev.next = nextt
            curr.next = None
        else:
            curr = head
            startCounter= 1
            prev = head
            while(startCounter < nodesNumToDel):
                prev = curr
                curr = curr.next
                startCounter += 1
            nextt = curr.next
            # print(nextt, 'check')
            if nodesNumToDel == 1:
                head = nextt
            else:                
                prev.next = nextt
                curr.next = None
        # print(prev, 'check', head)
        return head

# i did it by myself, wooohh and 88% faster+20%less memory use 
# so how i approached this prob,,, main task was to find how many nodes are there
# that we could have done by iterating to lineked list but that would have taken two pass
# to solve this questn so for one pass i used slow and fast pointer concept
# what i did, frstly find the middle and from middle and fast pointer pos i fount total nodes
# then found node to be delete pos from start i.e from last if its 2 and no of nodes is 5 then 
# 4th node mns we want to del from  start.. then i divided the array into two parts
# if nodetobedel post comes in between start to middle then frst half me i will iterate else
# later half me... i got stuck at frst node deleteion ...i got learning head j hai na frst node h hai
# head.next point nhi krta frst node k frstnode is head...thats why when to del
# frst node mns head should be curr.next...so this is whole
# time complexity as its in one pass meaning - o(n) 