# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node, d):
            if not node:
                return 0

            if not node.left and not node.right:
                return node.val if d == 0 else 0

            left = helper(node.left, 0)
            right = helper(node.right, 1)
            return right + left
        return helper(root, -1) 