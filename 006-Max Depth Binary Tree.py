# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case when we've reached the end of a node (no child)
        if not root:
            return 0
        # Recursive call, everytime we call it, we go one level below
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
