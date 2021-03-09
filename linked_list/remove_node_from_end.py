class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        countNodes = 0
        current = head
        while(current):
            countNodes += 1
            current = current.next
        nodeToBeDeleted = countNodes - n + 1
        current = head
        countNodes = 1
        while(current):
            if nodeToBeDeleted == 1:
                head = current.next
                break
            elif (countNodes + 1) == nodeToBeDeleted:
                print(current.val, countNodes)
                current.next = current.next.next
                break
            else:
                countNodes += 1
            current = current.next
        return head
            
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast_ptr = head
        slow_ptr = head
        for idx in range(n):
            fast_ptr = fast_ptr.next
        if fast_ptr == None:
            head = slow_ptr.next
            return head
        while fast_ptr.next:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return head