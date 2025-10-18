class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        

        points.sort(key=lambda t: t[0]**2 + t[1]**2)
        return points[:k]

