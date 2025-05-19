class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        lst = []
        lst2 = []
        for i in nums:
            if i not in lst:
                lst.append(i)
            
            else:
                lst2.append(i)
        if len(lst2) > 0:
            return True
        else:
            return False
