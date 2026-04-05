# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # highest common ancestor is root
        # we check if p.val and q.val > root, then we go down to the right else go down to left, if p.val <= root.val <= q.val, return root
        if root.val == p.val or root.val == q.val:
            return root
        if p.val < root.val and root.val < q.val or q.val < root.val and root.val < p.val:
            return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q) 