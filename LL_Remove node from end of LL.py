# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # barti

        ## 1. we compute length of list
        ## 2. compute  c - n -- the node we want to delete
        ## 3. delete that node by using pointers. 
        c = 0
        curr = head
        while curr:
            c+=1
            curr = curr.next
        
        print("length: ", c)

        comp = c - n
        if comp == 0:
            return head.next
        curr = head
        for _ in range(comp - 1):
            curr = curr.next
        
        # Step 4: Remove the nth node from end
        curr.next = curr.next.next
        
        return head
            

            


