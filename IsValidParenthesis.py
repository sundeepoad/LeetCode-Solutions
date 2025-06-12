class Solution:
    def isValid(self, s: str) -> bool:
        
        lst = []
        if len(s) == 0 or len(s) == 1:
            return False
        for i in s:
            if i == "(" or  i == "{" or  i == "[":
                lst.append(i)
   
            if i == ")" and lst and  lst[-1] == "(" and len(lst) > 0:
                lst.pop()
            elif i == "}" and lst and lst[-1] == "{" and len(lst) > 0:
                lst.pop()
            
            elif i == "]" and lst and lst[-1] == "[" and len(lst) > 0:
                lst.pop()
        
            elif i == "]" or i == "}" or i == ")" and len(lst) == 0:
                return False

  
        if len(lst) == 0:
            return True
        
        else:
            return False
