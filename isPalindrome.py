class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lst = []
        for i in s:
            if i.isalnum() == True:
                lst.append(i)
        
        new = ''.join(lst)
        new = new.lower()

        return new == new[::-1]
