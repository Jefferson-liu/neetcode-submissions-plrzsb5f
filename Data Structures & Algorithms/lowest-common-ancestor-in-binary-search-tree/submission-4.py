# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def isParent(root, child):
            if root is None:
                return False
            if child.val == root.val:
                return True
            else:
                return isParent(root.left, child) or isParent(root.right, child)
            
        
        queue = deque([root])
        parent = root
        while queue:
            cur = queue.popleft()
            if isParent(cur, p) and isParent(cur, q):
                parent = cur
            if cur.left and q.val <= cur.val and p.val <= cur.val:
                queue.append(cur.left)
            if cur.right and q.val >= cur.val and p.val >= cur.val:
                queue.append(cur.right)
        return parent