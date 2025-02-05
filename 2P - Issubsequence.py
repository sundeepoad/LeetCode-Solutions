class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        a = 0
        b = 0
        if len(list(t)) < len(list(s)):
                return False
        for i in range(len(t)):
            if a == len(list(s)):
                return True
            if t[i] == s[a]:
                a = a+1
            else:
                b+=1
        if a == len(list(s)):
            return True
        else:
            return False
            
