class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        final = []
  
        p1 = 0
        p2 = len(heights) -1

        while p1 < p2:

            area = (p2 - p1) * min(heights[p1],heights[p2])
            final.append(area)

            if heights[p1] < heights[p2]:
                p1+=1
            
            else:
                p2-=1

        return max(final)
