# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    def traverse(self, root):
        # this will just traverse the tree in-order
        if root == None:
            return ["N"]
        return  [str(root.val)] + self.traverse(root.left) + self.traverse(root.right)
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        return " ".join(self.traverse(root))

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #print(data)
        vals = data.split()
        self.index = 0
        def dfs():
            if vals[self.index] == "N":
                self.index += 1
                return None
            node = TreeNode(int(vals[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
            

            
            

            