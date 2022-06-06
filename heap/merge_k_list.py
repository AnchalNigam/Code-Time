# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from heapq import *
from typing import List, Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for list_idx, node in enumerate(lists):
            if node is not None:
                heappush(heap, (node.val, list_idx, node))
        result = ListNode()
        head = result
        while heap:
            val, i, node = heappop(heap)
            if result is None:
                result = ListNode(val)
            else:
                result.next = ListNode(val)
                result = result.next
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        return head.next
        
# main funda i used of heap...mostly solved by own...in mid refer bt majorly my logic
# so here basic funda is picked 1st elem of list and put it in heap
# after popping checking kya iska next elem hai ..aisa h skta h next elem list k frst elem se
# smaller h so again pushed so again poped and making reuslt linkedlist along with
# tc - n*logk as k size ka h heap banega , k is ur list length and n elems ie. all elem
# of linkedlist we are traversing and poping pushing so nlogk major
# space is o(k)