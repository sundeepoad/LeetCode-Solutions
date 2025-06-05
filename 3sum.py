nums = [-1,0,1,2,-1,-4]
nums1=[0,1,1]

def threeSum(nums):

            
    p1 = 0
    p2 = 1

    while p1 < len(nums):
        p2 = p1 + 1

        while p2 < len(nums):
            p3 = p2+ 1

            while p3 < len(nums):

                if nums[p1] + nums[p2] + nums[p3] == 0:
                    
                    return [nums[p1],nums[p2], nums[p3]]
                    
                else:
                    p3 +=1
                
            p2 +=1
            
        p1 +=1              

print(threeSum(nums1))
