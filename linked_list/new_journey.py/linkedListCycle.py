# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        slow_ptr = head
        fast_ptr = head.next
        
        while(slow_ptr != fast_ptr):
            if fast_ptr == None or fast_ptr.next == None:
                return False
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return True

# next verson mine

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
            
        slow = head
        fast = head.next
        
        while(fast and fast.next):
            if(slow == fast):
                return True
            slow = slow.next
            fast = fast.next.next
        return False
            