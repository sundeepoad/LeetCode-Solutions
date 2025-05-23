class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ## dictionary for occurence.
        ## keep removing t elements
        lst_s = list(s)
        lst_t = list(t)

        if len(lst_s) != len(lst_t):
            return False

        for i in lst_t:
            if i in lst_s:
                lst_s.remove(i)
        print(lst_s)
        if len(lst_s) == 0:
            return True
        else:
            return False
