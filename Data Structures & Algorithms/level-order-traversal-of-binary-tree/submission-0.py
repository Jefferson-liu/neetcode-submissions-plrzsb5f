# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this must be bfs, we queue the left and right of the node into a new list
        queue = deque([(root, 0)])
        levels = defaultdict(list)
        if not root:
            return []
        while queue:
            node, level = queue.pop()
            levels[level].append(node.val)
            if node.left:
                queue.appendleft((node.left, level + 1))
            if node.right:
                queue.appendleft((node.right, level + 1))
        return [x for x in levels.values()]
