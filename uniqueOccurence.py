arr = [1,2,3] 

class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        
        ### count frequencies
        ## if all values in dictionary are unique return true else false
        

        lst1 = {}
        for i in arr:
            if i in lst1:
                lst1[i] +=1
            else:
                lst1[i] = 1
        
        final = []
        for i in lst1:
            if lst1[i] in final:
                return False
            
            else:
                final.append(lst1[i])
        return True

