# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(root1):
            if root1 is None:
                return []
            ls = traverse(root1.left)
            ls.append(root1.val)
            ls.extend(traverse(root1.right)) 
            return ls
        return traverse(root)[k-1]
            
                

