# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # queue, put left and right into the queue, also add 1
        if not root:
            return 0
        queue = deque([(root, 1)])
        maxDepth = 1
        while queue:
            node, depth = queue.pop()
            if node.left:
                queue.appendleft((node.left, depth + 1))
            if node.right:
                queue.appendleft((node.right, depth + 1))

            if depth > maxDepth: maxDepth = depth

        return depth

