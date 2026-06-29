# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # how do I check if its visible from the right? 
        # store the rightmost node of each layer

        q = deque([(root, 0)])
        ans = []
        if not root:
            return []
        while q:
            cur, l = q.popleft()
            if q and q[0][1] > l or len(q) == 0:
                ans.append(cur.val)
            if cur.left:
                q.append((cur.left, l + 1))
            if cur.right:
                q.append((cur.right, l + 1))
        return ans