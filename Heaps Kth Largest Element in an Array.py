class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = sorted(nums)
        rev = (n[::-1])
        return rev[k-1]

        
