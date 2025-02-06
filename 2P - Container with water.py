class Solution:
    def maxArea(self, height: List[int]) -> int:
        
## start 1 pointer from 0 index , 2nd from last index
## calculate volume and store in another array
##  do this until both pointers meet
## return max from final array

## formula: min(index 1, index 2) * (difference of indexes)

        p1 = 0
        p2 = len(height)-1
        lst = []

   

        while p1 < p2:
            
            vol = min(height[p1],height[p2]) * (p2 - p1)
            print("volume", vol)
            lst.append(vol)
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -=1
        
        p = 0
        for i in lst:
            if i > p:
                p = i
        

        return p




