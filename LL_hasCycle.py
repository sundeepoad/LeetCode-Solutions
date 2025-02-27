class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        lst = []
        while head:
            if head not in lst:
                lst.append(head)
                
            elif head in lst:
                return True
            
            head = head.next
      
        return False
            
