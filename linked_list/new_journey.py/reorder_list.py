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

# new approach without slow fast pointer
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        curr = head
        head2 = None
        count = 0
        while curr:
            node = ListNode(curr.val)
            if head2 is None:
                head2 = node
                temp = head2
            else:
                temp.next = node
                temp = temp.next
            count += 1
            curr = curr.next
        curr2 = head2
        prev = None
        while curr2:
            nextNode = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = nextNode

        head2 = prev
        curr = head
        curr2 = head2
        while curr2:
            # print(curr2.val)
            curr2 = curr2.next
        curr2 = head2
        # print(count, 'kkk')
        c = 0
        while curr  and curr2:
            c += 1
            if c > count//2:
                break
            nextNode1 = curr.next
            # print(nextNode1.val, curr.val,'check')
            nextNode2 = curr2.next
            # print(curr2.val, nextNode2.val, 'next2')
            curr.next = curr2
            curr2.next = nextNode1
            curr = nextNode1
            curr2 = nextNode2
        c = 0
        # print(count, 'check')
        curr = head
        while c < count-1:
            c += 1
            curr = curr.next
        curr.next = None

       