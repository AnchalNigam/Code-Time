# o(n) O(n)
def reverseLinkedList(self, head: ListNode) -> tuple:
    current = head
    prev = None
    nodesVal = ""
    while current:
        nodesVal += str(current.val)
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    head = prev
    return (nodesVal, head)
    
  def isPalindrome(self, head: ListNode) -> bool:
    nodesVal, head = self.reverseLinkedList(head)
    
    reverseNodesVal, head = self.reverseLinkedList(head)
  
    if nodesVal == reverseNodesVal:
        return True
    return False

# O(1), O(n)
class Solution:
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        head = prev
        return head
        
    def isPalindrome(self, head: ListNode) -> bool:
        if(head == None or head.next == None):
            return True
        high_ptr = head
        slow_ptr = head
        first_list = slow_ptr
        while(True):
            high_ptr = high_ptr.next.next
            if(high_ptr == None):
                second_list = slow_ptr.next
                break
                
            if(high_ptr.next == None):
                second_list = slow_ptr.next.next
                break
            
            slow_ptr = slow_ptr.next
        slow_ptr.next = None
        reverse_list = self.reverseLinkedList(second_list)
        
        isPalin = True
        while(first_list and reverse_list):
            if(first_list.val != reverse_list.val):
                isPalin = False
                break
            first_list = first_list.next
            reverse_list = reverse_list.next
        if isPalin:
            return True
        return False
        



      
      