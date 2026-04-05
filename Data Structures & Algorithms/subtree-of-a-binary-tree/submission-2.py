# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def stringTree(root1):
            if not root1:
                return ["N"]
            else:
                cur = [str(root1.val)]
                cur.extend(stringTree(root1.left))
                cur.extend(stringTree(root1.right))
            return cur
        
        print(stringTree(root))
        print(stringTree(subRoot))

        s1 = ' '.join(stringTree(root))
        s2 = ' '.join(stringTree(subRoot))
        return s2 in s1

