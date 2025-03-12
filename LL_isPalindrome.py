class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        current = head
        final = []

        while current:
            final.append(current.val)
            current = current.next

        current = head

        while current:
            new = current.next
            current.next = prev
            prev = current
            current = new
        

        final1 = []

        while prev:
            final1.append(prev.val)
            prev = prev.next

        print(final)
        print(final1)

        return final == final1class Solution:
   
