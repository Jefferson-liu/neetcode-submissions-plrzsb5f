# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        def minmaxVal(root):
            if root is None:
                return (-math.inf, math.inf)
            if root.left is None and root.right is None:
                return (root.val, root.val)
            else:
                return (max([root.val, minmaxVal(root.left)[0], minmaxVal(root.right)[0]]), min(root.val, minmaxVal(root.left)[1], minmaxVal(root.right)[1]))
        


        def dfs(root):
            if root is None:
                return True
            else:
                isLeft = True
                isRight = True
                if root.left:
                    isLeft = root.val > minmaxVal(root.left)[0]
                if root.right:
                    isRight = root.val < minmaxVal(root.right)[1]
                return isLeft and isRight and dfs(root.left) and dfs(root.right)

        return dfs(root)
