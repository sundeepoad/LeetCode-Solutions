# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ## add all nodes in a list. sort it. make a new linkedlist.
        
        lst = []
        
        for i in lists:
            while i:
                lst.append(i.val)
                i = i.next
        print(lst)

        lst.sort()

        ll = ListNode(0)
        curr = ll

        for value in lst:
            curr.next = ListNode(value)
            curr = curr.next
        return ll.next
