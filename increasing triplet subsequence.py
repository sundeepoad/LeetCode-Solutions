"""
Given an integer array nums, return true if there exists
a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        

        # compare 2 elements, if i<j add to a lst.
        ## compare enxt elemtns if j<k add to lst.
        ## if not, empty the lst.
        ## if list at end is not empty, return true else false
   
        one = float('inf')
        two = float('inf')

        for i in nums:
            if i <= one:
                one = i
            elif i <= two:
                two = i
            else:
                return True
        
        return False
