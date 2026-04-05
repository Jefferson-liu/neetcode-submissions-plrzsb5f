# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # new function: is same bin tree, then bfs and find all roots with same value of subroot
        def isSameTree(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 and not root2 or root2 and not root1:
                return False
            if root1 and root2 and root1.val == root2.val:
                return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
            else:
                return False
            
        queue = deque([root])
        while queue:
            node = queue.pop()
            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                        return True
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
                

        return False

