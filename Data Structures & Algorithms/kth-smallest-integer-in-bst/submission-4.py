# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # base case where root is none
        # ls = [traverse on root left]
        # ls.append(root value)
        # extend to have traversal on root.right
        ls = []
        def traverse(root1):
            if root1 is None:
                return 
            traverse(root1.left)
            ls.append(root1.val)
            traverse(root1.right)
        traverse(root)

        #print(ls)
        return ls[k-1]

        

            
                

