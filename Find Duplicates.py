class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        hp = {}
        
        for i in range(len(nums)):
            if nums[i] in hp:
                hp[nums[i]] += 1
            else:
                hp[nums[i]] = 1

        print(hp)

            

        for k,v in hp.items():
            if v > 1:
                return k
            
            
