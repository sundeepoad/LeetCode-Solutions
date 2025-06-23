class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #barti
        left = 1
        right = max(piles)
        res = right
        

        while left <= right:
            mid = (left + right) // 2
            total = 0

            for i in piles:
                total += math.ceil(i / mid)
            

            if total <= h:
                res = min(res,mid)
                right = mid - 1
                   
            else:
                left = mid + 1
                
        print(res)
        return res
