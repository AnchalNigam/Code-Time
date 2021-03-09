class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dic = {}
        current = head
        while(current):
            if current in dic:
                return True
            else:
                dic[current] = True
            current = current.next
        return False
        

