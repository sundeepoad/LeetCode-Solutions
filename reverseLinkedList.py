# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            new = current.next # (2)
            current.next = prev ## pre  = 2
            prev = current # prev = 1
            current = new # current = 2
        return prev

        
    
