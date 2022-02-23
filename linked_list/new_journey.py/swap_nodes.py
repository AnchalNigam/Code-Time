def swapNodes(head):
  if (head == None or head.next==None):
      return head
  tempNext = head.next.next
  tempFirst = head.next
  tempSecond = head
  head = tempFirst
  head.next = tempSecond
  head.next.next = swapNodes(tempNext)
  return head
  


  # https://leetcode.com/problems/swap-nodes-in-pairs/discuss/265325/Java-recursive-solution-beats-100-with-explanation
  # goood approach recursion(thought of just for one node swapping and then ecursviely done)