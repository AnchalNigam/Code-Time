class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        merged = head
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next
        if l1 != None:
            merged.next = l1
            merged = merged.next
        if l2 != None:
            merged.next = l2
            merged = merged.next
        return head.next
        
        