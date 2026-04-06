# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # [1,2,3,4]
        # [2,1,3,4]
        # root is always at preorder[0]
        # if we look at the inorder, we know that there is 1 to the left and 2 to the right 
        # i.e left = [2], right = [3,4]
        # then root of left is 2, root of right is 3 
        # so we can recursively iterate through 
        if not preorder or not inorder:
            return None
        val = preorder[0]
        rootIndex = inorder.index(val)
        root = TreeNode(val)
        root.left = self.buildTree(preorder[1:rootIndex + 1],inorder[:rootIndex])
        root.right = self.buildTree(preorder[rootIndex + 1:], inorder[rootIndex + 1:])
        return root

