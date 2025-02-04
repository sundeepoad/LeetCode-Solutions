class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lst = len(nums)
        for i in nums:
            if i == 0:
                nums.insert(lst,0)
                nums.remove(0)
        print(nums)
                
        
  
      
