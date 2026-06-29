# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #recursion

        def depth(root, k):
            if root is None:
                return k
            else:
                return max(depth(root.left, k + 1), depth(root.right, k + 1))
        
        return depth(root, 0)