# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        

        if not subRoot:
            return True
        if not root:
            return False

        if self.sametree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot))  
    
    def sametree(self,r,sr):
        if not r and not sr:
            return True
        
        if r and sr and r.val == sr.val:
            return ((self.sametree(r.left,sr.left)) and (self.sametree(r.right,sr.right)))
        
        return False
    
