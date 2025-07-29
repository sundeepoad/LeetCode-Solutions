class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # barti
        dic = {}
        stack = []

        for curr in nums2: 
            while stack and curr > stack[-1]:
                stack_elem = stack.pop()
                dic[stack_elem] = curr
            stack.append(curr)

        print("Stack: ", stack)
        res = []
        for i in stack:
            dic[i] = -1
        
        print(dic.items())
       
        for i in nums1:
            res.append(dic[i])
        return res
