# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ## where values of both lists start matching
        #, its intersect.

        ## intersection occurs when value at pointer l1
        ## and value at pointer l2 is same. 
        ## so we keep traversing the lists unless both match
        ## the same value
        ## if they don't match None is returned.
        if not headA or not headB:
            return None
        
        l1 = headA
        l2 = headB

        while l1 != l2:
            l1 = headB if l1 is None else l1.next
            l2 = headA if l2 is None else l2.next
        return l1

    

