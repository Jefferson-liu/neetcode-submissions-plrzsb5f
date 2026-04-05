# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def traverse(root1, depth, ls):
            if root1 is None:
                return None
            else:
                if len(ls) == depth:
                    ls.append([])

                ls[depth].append(root1.val)
                traverse(root1.left, depth + 1, ls)
                traverse(root1.right, depth + 1, ls)
        traverse(root, 0, ans)
        return ans
