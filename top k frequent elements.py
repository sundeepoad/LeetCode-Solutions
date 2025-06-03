class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ## make dictionary and save frequency.
        ## return frequency of top k elements.
        ## return key of top k items with higher values


        dic = {}
        lst = []

        for i in nums:

            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        
        

        top = dict(sorted(dic.items(), key = lambda item: item[1], reverse = True)[:k])

        return list(top)
