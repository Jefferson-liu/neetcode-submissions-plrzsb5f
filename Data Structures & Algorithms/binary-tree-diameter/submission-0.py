# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # recursion
        maxVal = 0
        def height(root):
            if root is None:
                return 0
            else:
                # we find the longest path
                return 1 + max(height(root.left), height(root.right))
        
        
        q = deque([root])
        
        while q:
            head = q.popleft()
            maxVal = max(maxVal, height(head.left) + height(head.right))
            if head.left:
                q.append(head.left)
            if head.right:
                q.append(head.right)
        return maxVal
        
        