# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # print('isnid', slow, fast)
                break
        # this is for no cycle case
        if((fast is None) or (fast.next is None)):
            return None
        fast = head
        while(slow != fast):
            slow = slow.next
            fast = fast.next
        return fast
        
# in this we have firstly fnd where they meet..once we find, we then reset one pointer to start
# and then again pointer move start to again meet them .(interestng)