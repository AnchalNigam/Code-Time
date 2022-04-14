# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        slow = head
        fast = head
        start = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        last = ListNode()
        prev = slow
        while(curr):
            if(curr.next is None):
                last = curr
            nextt = curr.next
            curr.next = prev
            prev = curr           
            curr = nextt
        # print(slow.val, 'middle', last.next.val)
        while(start != slow):
            # print(start.val, last.val)
            if start.val != last.val:
                return False
            last = last.next
            start = start.next
      
        return True

# here o(n), o(1) space
# main thought is frst find middle of linked list
# then after that wale list k reverse kr do
# then start and last k compare kro and thats it