class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        
        #print(int(mid))
        ## sol 1:
     #   for i, v in enumerate(nums):
      #      if v == target:
       #         return i
       # return -1

        ## sol2:
        left = 0
        right = len(nums) - 1 

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            
            elif nums[mid] < target:
                left = mid + 1

            else:
                return mid
        
        return -1
