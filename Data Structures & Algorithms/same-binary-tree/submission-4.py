# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def checkSame(p, q):

            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            
            if p.val != q.val:
                return False
            else:
                return checkSame(p.left, q.left) and checkSame(p.right, q.right)
        
        return checkSame(p, q)