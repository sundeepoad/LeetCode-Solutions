class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ## start p1, and p2 would be p1+ 1
        ## keep p1 fixed and check all the remaining values.
        ## if not found, move p1 by 1 step and reset p2 with the
        ## next index as p1
        
        p1 = 0
        
        while p1 < len(numbers):
            p2 = p1 + 1
        
            while p2 < len(numbers) and p1 < p2:
                if numbers[p1] + numbers[p2] == target:
                    return [p1+1, p2+1]
                else:
                    p2 +=1
        
            p1 +=1
