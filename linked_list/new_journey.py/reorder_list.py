# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        slow = head
        fast = head
        start = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        last = ListNode()
        prev = None
        while(curr):
            nextt = curr.next
            curr.next = prev
            prev = curr           
            curr = nextt
        slow.next = None
        last = prev
        while start and last:
            nxt1 = start.next
            nxt2 = last.next
            start.next = last
            start = nxt1
            last.next = start
            last = nxt2
      

# main thought is frst find middle of linked list
# then after that wale list k reverse kr do
# then start and last k merge kro and thats it