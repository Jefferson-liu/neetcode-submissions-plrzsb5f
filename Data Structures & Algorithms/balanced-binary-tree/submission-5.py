class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if node is None:
                return 0                 # height of empty tree
            lh = check(node.left)
            if lh == -1: return -1       # left already unbalanced, bubble it up
            rh = check(node.right)
            if rh == -1: return -1
            if abs(lh - rh) > 1:
                return -1                # imbalance found here
            return 1 + max(lh, rh)       # otherwise return real height
        return check(root) != -1