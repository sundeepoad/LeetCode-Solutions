class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ## first we convert into set to remove duplicates and sort.
        ## if there is not i - 1, then it becomes 1st elem of our sequence.
        ## as long as we have i + l it becomes part of our sequence and adds to length of sequence.
        
        
        myset = set(nums)
        print(myset)
        longest = 0

        for i in myset:
            if (i - 1) not in myset:
                l = 1
            
                while (i + l) in myset:
                    l +=1 
                longest = max(l, longest)
        return longest
