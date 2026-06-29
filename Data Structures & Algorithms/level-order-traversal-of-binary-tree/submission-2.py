# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root, 0)])

        ans = []
        while q:
            cur, layer = q.popleft()
            if len(ans) == layer:
                ans.append([])
            ans[-1].append(cur.val)
            if cur.left:
                q.append((cur.left, layer + 1))
            if cur.right:
                q.append((cur.right, layer + 1))
        return ans