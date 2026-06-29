# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(cur, largest):
            if not cur:
                return 0
            if largest <= cur.val:
                return 1 + dfs(cur.right, cur.val) + dfs(cur.left, cur.val)
            else:
                return dfs(cur.right, largest) + dfs(cur.left, largest)
        return dfs(root, float('-inf'))