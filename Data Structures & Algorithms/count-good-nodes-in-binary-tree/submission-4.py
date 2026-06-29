# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodCounter(root, maxVal):
            if root is None:
                return 0
            if root.val >= maxVal:
                return 1 + goodCounter(root.left, root.val) + goodCounter(root.right, root.val)
            else:
                return goodCounter(root.left, maxVal) + goodCounter(root.right, maxVal)
        
        return goodCounter(root, root.val)
        

            
