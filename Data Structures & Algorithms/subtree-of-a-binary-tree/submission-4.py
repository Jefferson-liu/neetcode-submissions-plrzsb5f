# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(p, s):
            # s is the subtree
            if p is None and s is None:
                return True
            elif s is not None and p is None:
                return False
            elif s is None and p is not None:
                return False
            
            if p.val != s.val:
                return False
            return isSame(p.left, s.left) and isSame(p.right, s.right)

        q = deque([root])

        while q:
            cur = q.popleft()
            if cur.val == subRoot.val:
                if isSame(cur, subRoot):
                    return True
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return False