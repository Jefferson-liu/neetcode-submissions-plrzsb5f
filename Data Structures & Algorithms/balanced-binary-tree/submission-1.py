# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if root is None:
                return 0
            else:
                return 1 + max(height(root.left), height(root.right))
        if not root:
            return True
        q = deque([root])
        while q:
            cur = q.popleft()
            if abs(height(cur.left) - height(cur.right)) > 1:
                return False
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return True