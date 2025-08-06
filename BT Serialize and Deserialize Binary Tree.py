# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encode = []
        def dfs(root):
            if not root:
                encode.append("N")
                return
            
            encode.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return encode
        
        dfs(root)
        return ",".join(encode)
            


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        values = data.split(",")
        self.index = 0

        def dfs():
            if self.index >= len(values):
                return None
            
            val = values[self.index]
            self.index +=1

            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()

